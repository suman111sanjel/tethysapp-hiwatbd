export var TethysAppName="regionaldrought";


let ThreddsServerVar=null;
if (process.env.NODE_ENV === "production") {

    ThreddsServerVar='http://172.16.2.170:8080/thredds';

} else {

        ThreddsServerVar='http://tethys.icimod.org:8080/thredds'

}


export const ThreddsServer=ThreddsServerVar;