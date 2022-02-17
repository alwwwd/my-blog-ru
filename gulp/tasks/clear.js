const del = require ("del");
const path = require("../config/path.js");


const clear = ()=>{
    return del("./dist")
  }

module.exports = clear;
  