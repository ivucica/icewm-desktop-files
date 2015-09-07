#!/usr/bin/env python
import os
import os.path
import sys

import xdg.BaseDirectory
import xdg.DesktopEntry
from operator import methodcaller

def all_desktop_files(path=None):
    if not path:
        for path in xdg.BaseDirectory.xdg_data_dirs:
            for app in all_desktop_files(path):
                yield app
        return

    path = os.path.join(path, 'applications')
    if not os.path.exists(path):
        return

    all_files = [f for f in os.listdir(path)
                 if os.path.isfile(os.path.join(path, f))]
    desktop_files = [f for f in all_files if f.endswith('.desktop')]

    for desktop_file in desktop_files:
        yield os.path.join(path, desktop_file)

def all_apps():
    for desktop_file in all_desktop_files():
        desktop_entry = xdg.DesktopEntry.DesktopEntry(desktop_file)
        if desktop_entry.getType() != 'Application':
            continue
        yield desktop_entry


def all_desktop_directory_files(path=None):
    if not path:
        for path in xdg.BaseDirectory.xdg_data_dirs:
            for app in all_desktop_directory_files(path):
                yield app
        return

    path = os.path.join(path, 'desktop-directories')
    if not os.path.exists(path):
        return

    all_files = [f for f in os.listdir(path)
                 if os.path.isfile(os.path.join(path, f))]
    directory_files = [f for f in all_files if f.endswith('.directory')]

    for directory_file in directory_files:
        yield os.path.join(path, directory_file)


def all_desktop_directories():
    for directory_file in all_desktop_directory_files():
        directory_entry = xdg.DesktopEntry.DesktopEntry(directory_file)
        if directory_entry.getType() != 'Directory':
            continue
        directory_entry.path = directory_file
        yield directory_entry

def app_in_directory(app_entry, dir_entry):
    category = dir_entry.getName()
    return app_in_category(app_entry, category)

def app_in_category(app_entry, category):
    app = app_entry
    # TODO(ivucica): Verify notshowin does what I thought it does.
    if app.getNotShowIn() and category in app.getNotShowIn():
        return False
    if app.getOnlyShowIn() and 'Old' not in app.getOnlyShowIn():
        return False
    if app.getCategories() and category in app.getCategories():
        return True
    return False

def apps_in_directory(app_entries, dir_entry):
    for app in app_entries:
        if app_in_directory(app, dir_entry):
            yield app

def apps_in_category(app_entries, category):
    for app in app_entries:
        if app_in_category(app, category):
            yield app


def list_all_apps():
    for app in all_apps():
        print unicode(app).encode('utf-8')
def list_all_dirs():
    for dr in all_desktop_directories():
        print unicode(dr).encode('utf-8')

def list_apps_per_dir():
    all_apps_list = list(all_apps())
    for dr in all_desktop_directories():
        apps = list(apps_in_directory(all_apps_list, dr))
        if len(apps):
            print '[%s]' % dr.getName()
            print [app.getName() for app in apps]

def icewm_dirs():
    all_apps_list = list(all_apps())

    categories = ['AudioVideo', 'Audio', 'Video', 'Development', 'Education', 'Game', 'Graphics', 'Network', 'Office', 'Settings', 'System', 'Utility']
    for category in categories:
        apps = list(apps_in_category(all_apps_list, category))
	if len(apps):
            print 'menuprog "%s" folder "%s" "%s"' % (category, os.path.abspath(sys.argv[0]), category)

    all_desktop_directories_list = list(all_desktop_directories())
    list.sort(all_desktop_directories_list, key=methodcaller('getName'))

    for dr in all_desktop_directories_list:
        apps = list(apps_in_directory(all_apps_list, dr))
	if len(apps):
            print 'menuprog "%s" folder "%s" "%s"' % (dr.getName(), os.path.abspath(sys.argv[0]), dr.path)

def icewm_apps(directory_file_or_category=None):
    all_apps_list = list(all_apps())
    if directory_file_or_category[0] == '/':
	directory_entry = xdg.DesktopEntry.DesktopEntry(directory_file_or_category)
	apps = list(apps_in_directory(all_apps_list, directory_entry))
    else:
	apps = list(apps_in_category(all_apps_list, directory_file_or_category))
    
    list.sort(apps, key=methodcaller('getName'))
    for app in apps:
        print 'prog "%s" "%s" %s' % (app.getName(), app.getIcon(), app.getExec().replace("%U", ""))

if len(sys.argv) > 1:
    icewm_apps(sys.argv[1])
else:
    icewm_dirs()
