export var TethysAppName="regionaldrought";


let ThreddsServerVar=null;
if (process.env.NODE_ENV === "production") {

    ThreddsServerVar='http://180.211.163.139:8080/thredds';

} else {

        ThreddsServerVar='http://180.211.163.139:8080/thredds'

}


export const ThreddsServer=ThreddsServerVar;