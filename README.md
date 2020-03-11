# home-assistant-blebox

Home Assistant BleBox integration (as a Home Assistant custom component).


NOTE: This is for people who can't wait for official BleBox support in Home Assistant.

(The PR for that is here: https://github.com/home-assistant/core/pull/32664)


NOTE: This plugin is still in beta.

(Though it IS expected to work perfectly - please (open an issue in the main repo) if not!)


NOTE: The repository for blebox_uniapi PyPI module (used by this integration) is here: https://github.com/gadgetmobile/blebox_uniapi/settings


## Instructions

1. Download: https://github.com/gadgetmobile/home-assistant-blebox/archive/0.0.1.zip

2. Unzip to your Home Assistant config dir in a `custom_components` subdirectory.

(e.g. you have `$HOME/.home-assistant/custom_components/blebox/air_quality.py`)

3. Start (or restart) your Home Assistant, as usual.

4. Add an integration, search for "BleBox"

5. Set the IP of the device and accept. (It should display the BleBox device name).

And your done!
