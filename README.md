# home-assistant-blebox

Home Assistant BleBox integration (as a Home Assistant custom component).


NOTE: This is for people who can't wait for the official BleBox support in Home Assistant.

(The PR for that is here: https://github.com/home-assistant/core/pull/32664)


NOTE: This plugin is still in beta.

(Though it IS expected to work perfectly - please open an issue if not!)


NOTE: The repository for blebox_uniapi PyPI module (used by this integration) is here: https://github.com/gadgetmobile/blebox_uniapi


## Instructions

1. Download the latest release: https://github.com/gadgetmobile/home-assistant-blebox/releases/latest

2. Unzip to your Home Assistant config dir in a `custom_components` subdirectory.

(e.g. rename/move the unzipped folder so you have `$HOME/.home-assistant/custom_components/blebox/manifest.json`)

3. Start (or restart) your Home Assistant, as usual.

4. Add an integration, search for "BleBox".

5. Set the IP of the device and accept. (It should display the BleBox device name upon success).

And you're done! (The new device's features should appear in the HASS dashboard).


## Troubleshooting

1. Check that your Home Assistant config directory has a path like this `$HOME/.home-assistant/custom_components/blebox/manifest.json`

2. Check that the above file requires the latest `blebox_uniapi` version, e.g.

```
"requirements": ["blebox_uniapi==0.1.1", "semver==2.9.1"],
```

3. Restart Home Assistant (if you have installed/updated any of the above)


4. Check your `blebox_uniapi` version used by Home Assistant:

Home Assistant -> Developer Tools -> Logs -> LOG FULL HOME ASSISTANT LOGS ...

... and you should see a matching blebox_uniapi version:


```
2020-03-17 04:19:56 INFO (SyncWorker_35) [homeassistant.util.package] Attempting install of blebox_uniapi==0.1.1
```

5. Remove the integration:

Home Assistant -> Configuration -> Integrations -> Configured -> (Trash bin icon)

6. Add the integration via UI:

Home Assistant -> Configuration -> Integrations -> (Big "+" Button) -> (search "blebox") -> add IP

7. Use the BleBox phone app to check whether the device state is being set correctly

8. If you have further issues, check Home Assistant logs for errors and crashes

9. If all above fails, open an issue here: https://github.com/gadgetmobile/blebox_uniapi/issues/new
