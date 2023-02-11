# Demo application with pyupdater(auto updating desktop application)

Getting started
1. Init pyupdater `pyupdater init` all need to enable and sign (urls for updates 0.0.0.0:8000, disable updating patch) 
2. Import keys `pyupdater keys -i`
3. Make spec file (need for build application) `pyupdater make-spec main.py --add-data App.qml:.`
4. Build app `pyupdater build --app-version=1.0.0`
5. Generate client config `pyupdater settings`
6. Prepare package `pyupdate pkg -p`
7. Sing package `pyupdater pkg -s`
8. Change version updater_launch/version.py 2.0.0
8. Repeat steps 4-7
9. Run small http server 0.0.0.0:8000 `python -m http.server -d pyu-date/deploy`
10. Copy archive and run application `cp ./pyu-data/files/LauncherApp-nix64-1.0.0.tar.gz . && tar -xzvf LauncherApp-nix64-1.0.0.tar.gz && ./LauncherApp/LauncherApp`