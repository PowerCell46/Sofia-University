import type { ExternalPluginConfig } from '@windy/interfaces';

const config: ExternalPluginConfig = {
    name: 'windy-plugin-my-plugin',
    version: '0.1.0',
    icon: '📍',
    title: 'GeoAI Point Picker',
    description: 'Pick a point on the map and submit it to the GeoAI application for analysis.',
    author: 'Peter Gerdzhikov',
    repository: 'https://github.com/windycom/windy-plugin-template',
    desktopUI: 'rhpane',
    mobileUI: 'fullscreen',
    routerPath: '/my-plugin',
    private: true,

    // Whenever user clicks on the map and the plugin is opened,
    // a singleclick event is emitted with the name of this plugin
    listenToSingleclick: true,

    // Adds the plugin to the map's right-click context menu,
    // so it can be opened directly with a LatLon parameter
    addToContextmenu: true,
};

export default config;
