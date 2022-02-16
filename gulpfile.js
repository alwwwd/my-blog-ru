

const { watch , series ,parallel } = require("gulp");
const gulp = require("gulp");
const scss = require("./gulp/tasks/scss.js")
const db =require("./gulp/tasks/db.js");
const clear = require ("./gulp/tasks/clear.js");
const html = require("./gulp/tasks/html.js");
const py = require("./gulp/tasks/py.js");
const img = require("./gulp/tasks/img.js");
const js = require("./gulp/tasks/js.js");
const fonts = require("./gulp/tasks/fonts.js");
const path = require("./gulp/config/path.js");




const watcher = () => {
    watch(path.watch.html, html ) 
    watch(path.watch.db, db)
    watch(path.watch.py ,py )
    watch(path.watch.scss , scss)
    watch(path.watch.img ,img)
    watch(path.watch.js ,js)
    watch(path.watch.fonts , fonts)
}

exports.watch = watch;
exports.html = html ;
exports.db = db;
exports.py = py;
exports.claer= clear;
exports.scss = scss;
exports.img = img;
exports.js = js;
exports.fonts = fonts;

exports.default = series(
  clear,
  fonts,
  parallel(html,scss,db,img,js,py,),
  

  watcher
  
);