(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0bcdae"],{"2a09":function(t,n,a){"use strict";a.r(n);var o=function(){var t=this,n=t.$createElement,a=t._self._c||n;return a("div",{staticClass:"pa-3"},[a("page-title",{attrs:{icon:"mdi-car"}},[t._v("탐사 차량")]),a("v-row",[a("v-col",{attrs:{cols:"12",sm:6}},[a("v-img",{attrs:{src:"http://192.168.117.10:8000/mjpeg/stream/","max-width":"640",contain:""}})],1),a("v-col",{staticClass:"text-center align-self-center",attrs:{cols:"6",sm:3}},[a("div",{staticClass:"my-3"},[a("knob",{attrs:{options:t.knobOptions},model:{value:t.angle,callback:function(n){t.angle=n},expression:"angle"}})],1),t._v(" "+t._s(t.angle.value)+"° ")]),a("v-col",{staticClass:"text-center align-self-center",attrs:{cols:"6",sm:3}},[a("direction-panel",{on:{direction:t.onDirection}})],1)],1)],1)},e=[],l={name:"ExplorationCar",data:function(){return{angle:{},knobOptions:[]}},computed:{},mounted:function(){for(var t=-90;t<=90;t+=5)this.knobOptions.push({value:t,label:t%20==0&&t,anchor:!0});this.angle.value=0},methods:{onDirection:function(t){console.log("direction:",t),this.$mqtt.publish("iot/hong/control/car",t)}},watch:{angle:function(){this.$mqtt.publish("iot/hong/control/camera",String(this.angle.value)),console.log("publish","iot/hong/control/camera",this.angle.value)}}},s=l,i=a("2877"),c=a("6544"),r=a.n(c),u=a("62ad"),p=a("adda"),d=a("0fd9"),g=Object(i["a"])(s,o,e,!1,null,null,null);n["default"]=g.exports;r()(g,{VCol:u["a"],VImg:p["a"],VRow:d["a"]})}}]);
//# sourceMappingURL=chunk-2d0bcdae.8e1070ff.js.map