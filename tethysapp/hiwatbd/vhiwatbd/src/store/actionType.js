// import {TethysAppName} from "../config";

let BaseUrl = null;

if (process.env.NODE_ENV === "production") {
        // BaseUrl = "http://localhost:8000";
    // BaseUrl = 'http://tethys.icimod.org';
    BaseUrl = 'http://172.16.2.170';
} else {
    BaseUrl = "http://localhost:8000";
}

export let Action = {
    Base: BaseUrl,
    // Base : 'http://110.44.114.244:8001/',
    SliceCatalog: "apps/regionaldrought/slicedfromcatalog",
    ForecastChartAPI: 'apps/regionaldrought/ajax/getspatialaverage/',
    CurrentChartAPI: 'apps/regionaldrought/ajax/getspatialaveragecurrent/',
    getCSRFToken: 'regionaldrought/getCSRFToken',
    LatestHIWATInfo:'apps/hiwatbd/getLatestHIWATInfo/',
};