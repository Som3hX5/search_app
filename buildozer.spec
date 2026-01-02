[app]
title = Search App
package.name = searchapp
package.domain = org.som3h
version = 0.1

source.dir = .
source.include_exts = py

requirements = python3,kivy,pyjnius==1.6.1

orientation = portrait

android.permissions = INTERNET
android.accept_sdk_license = True

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

fullscreen = 0
