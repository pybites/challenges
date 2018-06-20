(function(){var k,aa="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ba;
if("function"==typeof Object.setPrototypeOf)ba=Object.setPrototypeOf;else{var ca;a:{var da={bb:!0},ea={};try{ea.__proto__=da;ca=ea.bb;break a}catch(a){}ca=!1}ba=ca?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}
var fa=ba,ha="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)},ia="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this;
function ja(a,b){if(b){for(var c=ia,d=a.split("."),e=0;e<d.length-1;e++){var f=d[e];f in c||(c[f]={});c=c[f]}d=d[d.length-1];e=c[d];f=b(e);f!=e&&null!=f&&ha(c,d,{configurable:!0,writable:!0,value:f})}}
var ka=function(){function a(){function a(){}
Reflect.construct(a,[],function(){});
return new a instanceof a}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(a,d,e){a=b(a,d);e&&Reflect.setPrototypeOf(a,e.prototype);return a}}return function(a,b,e){void 0===e&&(e=a);
e=aa(e.prototype||Object.prototype);return Function.prototype.apply.call(a,e,b)||e}}();
ja("Reflect.construct",function(){return ka});
ja("Object.is",function(a){return a?a:function(a,c){return a===c?0!==a||1/a===1/c:a!==a&&c!==c}});
var m=this;function p(a){return void 0!==a}
function r(a){return"string"==typeof a}
function la(a){return"number"==typeof a}
function u(a){a=a.split(".");for(var b=m,c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function ma(){}
function oa(a){a.aa=void 0;a.v=function(){return a.aa?a.aa:a.aa=new a}}
function pa(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function qa(a){return"array"==pa(a)}
function ra(a){var b=pa(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function sa(a){return"function"==pa(a)}
function ta(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function ua(a){return a[va]||(a[va]=++wa)}
var va="closure_uid_"+(1E9*Math.random()>>>0),wa=0;function xa(a,b,c){return a.call.apply(a.bind,arguments)}
function ya(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function v(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?v=xa:v=ya;return v.apply(null,arguments)}
function za(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}}
var Aa=Date.now||function(){return+new Date};
function x(a,b){var c=a.split("."),d=m;c[0]in d||"undefined"==typeof d.execScript||d.execScript("var "+c[0]);for(var e;c.length&&(e=c.shift());)!c.length&&p(b)?d[e]=b:d[e]&&d[e]!==Object.prototype[e]?d=d[e]:d=d[e]={}}
function y(a,b){function c(){}
c.prototype=b.prototype;a.w=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Ob=function(a,c,f){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}}
;function Ba(a){if(Error.captureStackTrace)Error.captureStackTrace(this,Ba);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
y(Ba,Error);Ba.prototype.name="CustomError";var Ca;var Da=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(r(a))return r(b)&&1==b.length?a.indexOf(b,0):-1;
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},A=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=r(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Ea=Array.prototype.filter?function(a,b,c){return Array.prototype.filter.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=[],f=0,g=r(a)?a.split(""):a,h=0;h<d;h++)if(h in g){var l=g[h];
b.call(c,l,h,a)&&(e[f++]=l)}return e},Fa=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e=r(a)?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},Ga=Array.prototype.some?function(a,b){return Array.prototype.some.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=r(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a))return!0;
return!1};
function Ha(a,b){a:{var c=a.length;for(var d=r(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:r(a)?a.charAt(c):a[c]}
function Ia(a,b){return 0<=Da(a,b)}
function Ja(a){return Array.prototype.concat.apply([],arguments)}
function Ka(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function La(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(ra(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
function Ma(a,b,c,d){return Array.prototype.splice.apply(a,Na(arguments,1))}
function Na(a,b,c){return 2>=arguments.length?Array.prototype.slice.call(a,b):Array.prototype.slice.call(a,b,c)}
function Oa(a){for(var b=[],c=0;c<arguments.length;c++){var d=arguments[c];if(qa(d))for(var e=0;e<d.length;e+=8192)for(var f=Oa.apply(null,Na(d,e,e+8192)),g=0;g<f.length;g++)b.push(f[g]);else b.push(d)}return b}
;var Pa=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]},Qa=String.prototype.repeat?function(a,b){return a.repeat(b)}:function(a,b){return Array(b+1).join(a)};
function Ra(a){a=p(void 0)?a.toFixed(void 0):String(a);var b=a.indexOf(".");-1==b&&(b=a.length);return Qa("0",Math.max(0,2-b))+a}
function Sa(a,b){for(var c=0,d=Pa(String(a)).split("."),e=Pa(String(b)).split("."),f=Math.max(d.length,e.length),g=0;0==c&&g<f;g++){var h=d[g]||"",l=e[g]||"";do{h=/(\d*)(\D*)(.*)/.exec(h)||["","","",""];l=/(\d*)(\D*)(.*)/.exec(l)||["","","",""];if(0==h[0].length&&0==l[0].length)break;c=Ta(0==h[1].length?0:parseInt(h[1],10),0==l[1].length?0:parseInt(l[1],10))||Ta(0==h[2].length,0==l[2].length)||Ta(h[2],l[2]);h=h[3];l=l[3]}while(0==c)}return c}
function Ta(a,b){return a<b?-1:a>b?1:0}
function Ua(a){return String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()})}
function Va(a){var b=r(void 0)?"undefined".replace(/([-()\[\]{}+?*.$\^|,:#<!\\])/g,"\\$1").replace(/\x08/g,"\\x08"):"\\s";return a.replace(new RegExp("(^"+(b?"|["+b+"]+":"")+")([a-z])","g"),function(a,b,e){return b+e.toUpperCase()})}
;var Wa;a:{var Xa=m.navigator;if(Xa){var Ya=Xa.userAgent;if(Ya){Wa=Ya;break a}}Wa=""}function B(a){return-1!=Wa.indexOf(a)}
;function Za(a,b,c){for(var d in a)b.call(c,a[d],d,a)}
function $a(a){var b=[],c=0,d;for(d in a)b[c++]=a[d];return b}
function ab(a){var b=bb,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
var cb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function db(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<cb.length;f++)c=cb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;function eb(){return B("Safari")&&!(fb()||B("Coast")||B("Opera")||B("Edge")||B("Silk")||B("Android"))}
function fb(){return(B("Chrome")||B("CriOS"))&&!B("Edge")}
function gb(){return B("Android")&&!(fb()||B("Firefox")||B("Opera")||B("Silk"))}
;function hb(){return B("iPhone")&&!B("iPod")&&!B("iPad")}
function ib(){return hb()||B("iPad")||B("iPod")}
;function jb(a){jb[" "](a);return a}
jb[" "]=ma;function kb(a,b){var c=lb;return Object.prototype.hasOwnProperty.call(c,a)?c[a]:c[a]=b(a)}
;var mb=B("Opera"),C=B("Trident")||B("MSIE"),nb=B("Edge"),ob=nb||C,pb=B("Gecko")&&!(-1!=Wa.toLowerCase().indexOf("webkit")&&!B("Edge"))&&!(B("Trident")||B("MSIE"))&&!B("Edge"),qb=-1!=Wa.toLowerCase().indexOf("webkit")&&!B("Edge"),rb=B("Macintosh"),sb=B("Windows"),tb=B("Android"),ub=hb(),vb=B("iPad"),wb=B("iPod"),xb=ib();function yb(){var a=m.document;return a?a.documentMode:void 0}
var zb;a:{var Ab="",Bb=function(){var a=Wa;if(pb)return/rv:([^\);]+)(\)|;)/.exec(a);if(nb)return/Edge\/([\d\.]+)/.exec(a);if(C)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(qb)return/WebKit\/(\S+)/.exec(a);if(mb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
Bb&&(Ab=Bb?Bb[1]:"");if(C){var Cb=yb();if(null!=Cb&&Cb>parseFloat(Ab)){zb=String(Cb);break a}}zb=Ab}var Db=zb,lb={};function Eb(a){return kb(a,function(){return 0<=Sa(Db,a)})}
var Fb;var Gb=m.document;Fb=Gb&&C?yb()||("CSS1Compat"==Gb.compatMode?parseInt(Db,10):5):void 0;var Hb=!pb&&!C||C&&9<=Number(Fb)||pb&&Eb("1.9.1"),Ib=C&&!Eb("9");function Jb(){this.b="";this.f=Kb}
Jb.prototype.Z=!0;Jb.prototype.Y=function(){return this.b};
var Lb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i,Kb={};function Mb(a){var b=new Jb;b.b=a;return b}
Mb("about:blank");function Nb(){this.b="";this.f=Ob}
Nb.prototype.Z=!0;Nb.prototype.Y=function(){return this.b};
function Pb(a){if(a instanceof Nb&&a.constructor===Nb&&a.f===Ob)return a.b;pa(a);return"type_error:SafeHtml"}
var Ob={};function Qb(a){var b=new Nb;b.b=a;return b}
Qb("<!DOCTYPE html>");Qb("");Qb("<br>");function D(a,b){this.x=p(a)?a:0;this.y=p(b)?b:0}
D.prototype.equals=function(a){return a instanceof D&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
function Rb(a,b){return new D(a.x-b.x,a.y-b.y)}
D.prototype.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
D.prototype.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
D.prototype.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Sb(a,b){this.width=a;this.height=b}
k=Sb.prototype;k.eb=function(){return this.width*this.height};
k.aspectRatio=function(){return this.width/this.height};
k.isEmpty=function(){return!this.eb()};
k.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
k.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
k.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Tb(a){return a?new Ub(Vb(a)):Ca||(Ca=new Ub)}
function E(a){return r(a)?document.getElementById(a):a}
function Wb(a,b){var c=b||document;return c.querySelectorAll&&c.querySelector?c.querySelectorAll("."+a):Xb(document,"*",a,b)}
function F(a,b){var c=b||document;if(c.getElementsByClassName)c=c.getElementsByClassName(a)[0];else{c=document;var d=b||c;c=d.querySelectorAll&&d.querySelector&&a?d.querySelector(a?"."+a:""):Xb(c,"*",a,b)[0]||null}return c||null}
function Xb(a,b,c,d){a=d||a;b=b&&"*"!=b?String(b).toUpperCase():"";if(a.querySelectorAll&&a.querySelector&&(b||c))return a.querySelectorAll(b+(c?"."+c:""));if(c&&a.getElementsByClassName){a=a.getElementsByClassName(c);if(b){d={};for(var e=0,f=0,g;g=a[f];f++)b==g.nodeName&&(d[e++]=g);d.length=e;return d}return a}a=a.getElementsByTagName(b||"*");if(c){d={};for(f=e=0;g=a[f];f++)b=g.className,"function"==typeof b.split&&Ia(b.split(/\s+/),c)&&(d[e++]=g);d.length=e;return d}return a}
function Yb(a,b){Za(b,function(b,d){b&&b.Z&&(b=b.Y());"style"==d?a.style.cssText=b:"class"==d?a.className=b:"for"==d?a.htmlFor=b:Zb.hasOwnProperty(d)?a.setAttribute(Zb[d],b):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,b):a[d]=b})}
var Zb={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};function $b(a){a=a.document;a=ac(a)?a.documentElement:a.body;return new Sb(a.clientWidth,a.clientHeight)}
function bc(a){var b=cc(a);a=dc(a);return C&&Eb("10")&&a.pageYOffset!=b.scrollTop?new D(b.scrollLeft,b.scrollTop):new D(a.pageXOffset||b.scrollLeft,a.pageYOffset||b.scrollTop)}
function cc(a){return a.scrollingElement?a.scrollingElement:!qb&&ac(a)?a.documentElement:a.body||a.documentElement}
function dc(a){return a.parentWindow||a.defaultView}
function ac(a){return"CSS1Compat"==a.compatMode}
function ec(a){a&&a.parentNode&&a.parentNode.removeChild(a)}
function fc(a){return Hb&&void 0!=a.children?a.children:Ea(a.childNodes,function(a){return 1==a.nodeType})}
function gc(a){return ta(a)&&1==a.nodeType}
function hc(a,b){if(!a||!b)return!1;if(a.contains&&1==b.nodeType)return a==b||a.contains(b);if("undefined"!=typeof a.compareDocumentPosition)return a==b||!!(a.compareDocumentPosition(b)&16);for(;b&&a!=b;)b=b.parentNode;return b==a}
function Vb(a){return 9==a.nodeType?a:a.ownerDocument||a.document}
function ic(a,b){if("textContent"in a)a.textContent=b;else if(3==a.nodeType)a.data=String(b);else if(a.firstChild&&3==a.firstChild.nodeType){for(;a.lastChild!=a.firstChild;)a.removeChild(a.lastChild);a.firstChild.data=String(b)}else{for(var c;c=a.firstChild;)a.removeChild(c);a.appendChild(Vb(a).createTextNode(String(b)))}}
function jc(a,b){var c=[];return kc(a,b,c,!0)?c[0]:void 0}
function kc(a,b,c,d){if(null!=a)for(a=a.firstChild;a;){if(b(a)&&(c.push(a),d)||kc(a,b,c,d))return!0;a=a.nextSibling}return!1}
var lc={SCRIPT:1,STYLE:1,HEAD:1,IFRAME:1,OBJECT:1},mc={IMG:" ",BR:"\n"};function nc(a){var b;if((b="A"==a.tagName||"INPUT"==a.tagName||"TEXTAREA"==a.tagName||"SELECT"==a.tagName||"BUTTON"==a.tagName?!a.disabled&&(!oc(a)||pc(a)):oc(a)&&pc(a))&&C){var c;!sa(a.getBoundingClientRect)||C&&null==a.parentElement?c={height:a.offsetHeight,width:a.offsetWidth}:c=a.getBoundingClientRect();a=null!=c&&0<c.height&&0<c.width}else a=b;return a}
function oc(a){return C&&!Eb("9")?(a=a.getAttributeNode("tabindex"),null!=a&&a.specified):a.hasAttribute("tabindex")}
function pc(a){a=a.tabIndex;return la(a)&&0<=a&&32768>a}
function qc(a){if(Ib&&null!==a&&"innerText"in a)a=a.innerText.replace(/(\r\n|\r|\n)/g,"\n");else{var b=[];rc(a,b,!0);a=b.join("")}a=a.replace(/ \xAD /g," ").replace(/\xAD/g,"");a=a.replace(/\u200B/g,"");Ib||(a=a.replace(/ +/g," "));" "!=a&&(a=a.replace(/^\s*/,""));return a}
function rc(a,b,c){if(!(a.nodeName in lc))if(3==a.nodeType)c?b.push(String(a.nodeValue).replace(/(\r\n|\r|\n)/g,"")):b.push(a.nodeValue);else if(a.nodeName in mc)b.push(mc[a.nodeName]);else for(a=a.firstChild;a;)rc(a,b,c),a=a.nextSibling}
function sc(a,b,c,d){if(!b&&!c)return null;var e=b?String(b).toUpperCase():null;return tc(a,function(a){return(!e||a.nodeName==e)&&(!c||r(a.className)&&Ia(a.className.split(/\s+/),c))},!0,d)}
function G(a,b){return sc(a,null,b,void 0)}
function tc(a,b,c,d){a&&!c&&(a=a.parentNode);for(c=0;a&&(null==d||c<=d);){if(b(a))return a;a=a.parentNode;c++}return null}
function Ub(a){this.b=a||m.document||document}
Ub.prototype.getElementsByTagName=function(a,b){return(b||this.b).getElementsByTagName(String(a))};
Ub.prototype.createElement=function(a){return this.b.createElement(String(a))};
Ub.prototype.appendChild=function(a,b){a.appendChild(b)};
Ub.prototype.isElement=gc;/*
 gapi.loader.OBJECT_CREATE_TEST_OVERRIDE &&*/
var uc=window,vc=document,wc=uc.location;function xc(){}
var yc=/\[native code\]/;function H(a,b,c){return a[b]=a[b]||c}
function Ac(a){a=a.sort();for(var b=[],c=void 0,d=0;d<a.length;d++){var e=a[d];e!=c&&b.push(e);c=e}return b}
function Bc(){var a;if((a=Object.create)&&yc.test(a))a=a(null);else{a={};for(var b in a)a[b]=void 0}return a}
var Cc=H(uc,"gapi",{});var J;J=H(uc,"___jsl",Bc());H(J,"I",0);H(J,"hel",10);function Dc(){var a=wc.href;if(J.dpo)var b=J.h;else{b=J.h;var c=RegExp("([#].*&|[#])jsh=([^&#]*)","g"),d=RegExp("([?#].*&|[?#])jsh=([^&#]*)","g");if(a=a&&(c.exec(a)||d.exec(a)))try{b=decodeURIComponent(a[2])}catch(e){}}return b}
function Ec(a){var b=H(J,"PQ",[]);J.PQ=[];var c=b.length;if(0===c)a();else for(var d=0,e=function(){++d===c&&a()},f=0;f<c;f++)b[f](e)}
function Fc(a){return H(H(J,"H",Bc()),a,Bc())}
;function Gc(){this.b=("undefined"==typeof document?null:document)||{cookie:""}}
k=Gc.prototype;k.isEnabled=function(){return navigator.cookieEnabled};
k.set=function(a,b,c,d,e,f){if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');p(c)||(c=-1);e=e?";domain="+e:"";d=d?";path="+d:"";f=f?";secure":"";c=0>c?"":0==c?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Aa()+1E3*c)).toUTCString();this.b.cookie=a+"="+b+e+d+c+f};
k.get=function(a,b){for(var c=a+"=",d=(this.b.cookie||"").split(";"),e=0,f;e<d.length;e++){f=Pa(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
k.remove=function(a,b,c){var d=p(this.get(a));this.set(a,"",0,b,c);return d};
k.isEmpty=function(){return!this.b.cookie};
k.clear=function(){for(var a=(this.b.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=Pa(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var Hc=new Gc;Hc.f=3950;var Ic=H(J,"perf",Bc());H(Ic,"g",Bc());var Jc=H(Ic,"i",Bc());H(Ic,"r",[]);Bc();Bc();function Kc(a,b,c){b&&0<b.length&&(b=Lc(b),c&&0<c.length&&(b+="___"+Lc(c)),28<b.length&&(b=b.substr(0,28)+(b.length-28)),c=b,b=H(Jc,"_p",Bc()),H(b,c,Bc())[a]=(new Date).getTime(),b=Ic.r,"function"===typeof b?b(a,"_p",c):b.push([a,"_p",c]))}
function Lc(a){return a.join("__").replace(/\./g,"_").replace(/\-/g,"_").replace(/,/g,"_")}
;var Mc=Bc(),Nc=[];function Oc(a){throw Error("Bad hint"+(a?": "+a:""));}
Nc.push(["jsl",function(a){for(var b in a)if(Object.prototype.hasOwnProperty.call(a,b)){var c=a[b];"object"==typeof c?J[b]=H(J,b,[]).concat(c):H(J,b,c)}if(b=a.u)a=H(J,"us",[]),a.push(b),(b=/^https:(.*)$/.exec(b))&&a.push("http:"+b[1])}]);
var Pc=/^(\/[a-zA-Z0-9_\-]+)+$/,Qc=[/\/amp\//,/\/amp$/,/^\/amp$/],Rc=/^[a-zA-Z0-9\-_\.,!]+$/,Sc=/^gapi\.loaded_[0-9]+$/,Tc=/^[a-zA-Z0-9,._-]+$/;function Uc(a,b,c,d){var e=a.split(";"),f=e.shift(),g=Mc[f],h=null;g?h=g(e,b,c,d):Oc("no hint processor for: "+f);h||Oc("failed to generate load url");b=h;c=b.match(Vc);(d=b.match(Wc))&&1===d.length&&Xc.test(b)&&c&&1===c.length||Oc("failed sanity: "+a);return h}
function Yc(a,b,c,d){function e(a){return encodeURIComponent(a).replace(/%2C/g,",")}
a=Zc(a);Sc.test(c)||Oc("invalid_callback");b=$c(b);d=d&&d.length?$c(d):null;return[encodeURIComponent(a.pathPrefix).replace(/%2C/g,",").replace(/%2F/g,"/"),"/k=",e(a.version),"/m=",e(b),d?"/exm="+e(d):"","/rt=j/sv=1/d=1/ed=1",a.ja?"/am="+e(a.ja):"",a.Da?"/rs="+e(a.Da):"",a.Ma?"/t="+e(a.Ma):"","/cb=",e(c)].join("")}
function Zc(a){"/"!==a.charAt(0)&&Oc("relative path");for(var b=a.substring(1).split("/"),c=[];b.length;){a=b.shift();if(!a.length||0==a.indexOf("."))Oc("empty/relative directory");else if(0<a.indexOf("=")){b.unshift(a);break}c.push(a)}a={};for(var d=0,e=b.length;d<e;++d){var f=b[d].split("="),g=decodeURIComponent(f[0]),h=decodeURIComponent(f[1]);2==f.length&&g&&h&&(a[g]=a[g]||h)}b="/"+c.join("/");Pc.test(b)||Oc("invalid_prefix");c=0;for(d=Qc.length;c<d;++c)Qc[c].test(b)&&Oc("invalid_prefix");c=ad(a,
"k",!0);d=ad(a,"am");e=ad(a,"rs");a=ad(a,"t");return{pathPrefix:b,version:c,ja:d,Da:e,Ma:a}}
function $c(a){for(var b=[],c=0,d=a.length;c<d;++c){var e=a[c].replace(/\./g,"_").replace(/-/g,"_");Tc.test(e)&&b.push(e)}return b.join(",")}
function ad(a,b,c){a=a[b];!a&&c&&Oc("missing: "+b);if(a){if(Rc.test(a))return a;Oc("invalid: "+b)}return null}
var Xc=/^https?:\/\/[a-z0-9_.-]+\.google(rs)?\.com(:\d+)?\/[a-zA-Z0-9_.,!=\-\/]+$/,Wc=/\/cb=/g,Vc=/\/\//g;function bd(){var a=Dc();if(!a)throw Error("Bad hint");return a}
Mc.m=function(a,b,c,d){(a=a[0])||Oc("missing_hint");return"https://apis.google.com"+Yc(a,b,c,d)};
var cd=decodeURI("%73cript"),dd=/^[-+_0-9\/A-Za-z]+={0,2}$/;function ed(a,b){for(var c=[],d=0;d<a.length;++d){var e=a[d],f;if(f=e){a:{for(f=0;f<b.length;f++)if(b[f]===e)break a;f=-1}f=0>f}f&&c.push(e)}return c}
function fd(){var a=J.nonce;return void 0!==a?a&&a===String(a)&&a.match(dd)?a:J.nonce=null:vc.querySelector?(a=vc.querySelector("script[nonce]"))?(a=a.nonce||a.getAttribute("nonce")||"",a&&a===String(a)&&a.match(dd)?J.nonce=a:J.nonce=null):null:null}
function gd(a){if("loading"!=vc.readyState)hd(a);else{var b=fd(),c="";null!==b&&(c=' nonce="'+b+'"');vc.write("<"+cd+' src="'+encodeURI(a)+'"'+c+"></"+cd+">")}}
function hd(a){var b=vc.createElement(cd);b.setAttribute("src",a);a=fd();null!==a&&b.setAttribute("nonce",a);b.async="true";(a=vc.getElementsByTagName(cd)[0])?a.parentNode.insertBefore(b,a):(vc.head||vc.body||vc.documentElement).appendChild(b)}
function id(a,b){var c=b&&b._c;if(c)for(var d=0;d<Nc.length;d++){var e=Nc[d][0],f=Nc[d][1];f&&Object.prototype.hasOwnProperty.call(c,e)&&f(c[e],a,b)}}
function jd(a,b,c){kd(function(){var c=b===Dc()?H(Cc,"_",Bc()):Bc();c=H(Fc(b),"_",c);a(c)},c)}
function ld(a,b){var c=b||{};"function"==typeof b&&(c={},c.callback=b);id(a,c);var d=a?a.split(":"):[],e=c.h||bd(),f=H(J,"ah",Bc());if(f["::"]&&d.length){for(var g=[],h=null;h=d.shift();){var l=h.split(".");l=f[h]||f[l[1]&&"ns:"+l[0]||""]||e;var n=g.length&&g[g.length-1]||null,t=n;n&&n.hint==l||(t={hint:l,features:[]},g.push(t));t.features.push(h)}var z=g.length;if(1<z){var q=c.callback;q&&(c.callback=function(){0==--z&&q()})}for(;d=g.shift();)md(d.features,c,d.hint)}else md(d||[],c,e)}
function md(a,b,c){function d(a,b){if(z)return 0;uc.clearTimeout(t);q.push.apply(q,w);var d=((Cc||{}).config||{}).update;d?d(f):f&&H(J,"cu",[]).push(f);if(b){Kc("me0",a,I);try{jd(b,c,n)}finally{Kc("me1",a,I)}}return 1}
a=Ac(a)||[];var e=b.callback,f=b.config,g=b.timeout,h=b.ontimeout,l=b.onerror,n=void 0;"function"==typeof l&&(n=l);var t=null,z=!1;if(g&&!h||!g&&h)throw"Timeout requires both the timeout parameter and ontimeout parameter to be set";l=H(Fc(c),"r",[]).sort();var q=H(Fc(c),"L",[]).sort(),I=[].concat(l);0<g&&(t=uc.setTimeout(function(){z=!0;h()},g));
var w=ed(a,q);if(w.length){w=ed(a,l);var na=H(J,"CP",[]),T=na.length;na[T]=function(a){function b(){var a=na[T+1];a&&a()}
function c(b){na[T]=null;d(w,a)&&Ec(function(){e&&e();b()})}
if(!a)return 0;Kc("ml1",w,I);0<T&&na[T-1]?na[T]=function(){c(b)}:c(b)};
if(w.length){var zc="loaded_"+J.I++;Cc[zc]=function(a){na[T](a);Cc[zc]=null};
a=Uc(c,w,"gapi."+zc,l);l.push.apply(l,w);Kc("ml0",w,I);b.sync||uc.___gapisync?gd(a):hd(a)}else na[T](xc)}else d(w)&&e&&e()}
function kd(a,b){if(J.hee&&0<J.hel)try{return a()}catch(c){b&&b(c),J.hel--,ld("debug_error",function(){try{window.___jsl.hefn(c)}catch(d){throw c;}})}else try{return a()}catch(c){throw b&&b(c),c;
}}
Cc.load=function(a,b){return kd(function(){return ld(a,b)})};function nd(a,b){this.g=a;this.j=b;this.f=0;this.b=null}
nd.prototype.get=function(){if(0<this.f){this.f--;var a=this.b;this.b=a.next;a.next=null}else a=this.g();return a};
function od(a,b){a.j(b);100>a.f&&(a.f++,b.next=a.b,a.b=b)}
;function pd(a){m.setTimeout(function(){throw a;},0)}
var qd;
function rd(){var a=m.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!B("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow;a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host;a=v(function(a){if(("*"==d||a.origin==d)&&a.data==
c)this.port1.onmessage()},this);
b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});
if("undefined"!==typeof a&&!B("Trident")&&!B("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(p(c.next)){c=c.next;var a=c.la;c.la=null;a()}};
return function(a){d.next={la:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");
b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};
document.documentElement.appendChild(b)}:function(a){m.setTimeout(a,0)}}
;function sd(){this.f=this.b=null}
var ud=new nd(function(){return new td},function(a){a.reset()});
sd.prototype.add=function(a,b){var c=ud.get();c.set(a,b);this.f?this.f.next=c:this.b=c;this.f=c};
sd.prototype.remove=function(){var a=null;this.b&&(a=this.b,this.b=this.b.next,this.b||(this.f=null),a.next=null);return a};
function td(){this.next=this.scope=this.b=null}
td.prototype.set=function(a,b){this.b=a;this.scope=b;this.next=null};
td.prototype.reset=function(){this.next=this.scope=this.b=null};function vd(a,b){wd||xd();yd||(wd(),yd=!0);zd.add(a,b)}
var wd;function xd(){if(m.Promise&&m.Promise.resolve){var a=m.Promise.resolve(void 0);wd=function(){a.then(Ad)}}else wd=function(){var a=Ad;
!sa(m.setImmediate)||m.Window&&m.Window.prototype&&!B("Edge")&&m.Window.prototype.setImmediate==m.setImmediate?(qd||(qd=rd()),qd(a)):m.setImmediate(a)}}
var yd=!1,zd=new sd;function Ad(){for(var a;a=zd.remove();){try{a.b.call(a.scope)}catch(b){pd(b)}od(ud,a)}yd=!1}
;var Bd=B("Firefox"),Cd=hb()||B("iPod"),Dd=B("iPad"),Ed=gb(),Fd=fb(),Gd=eb()&&!ib();function Hd(a,b,c){la(a)?(this.date=Id(a,b||0,c||1),Jd(this,c||1)):ta(a)?(this.date=Id(a.getFullYear(),a.getMonth(),a.getDate()),Jd(this,a.getDate())):(this.date=new Date(Aa()),a=this.date.getDate(),this.date.setHours(0),this.date.setMinutes(0),this.date.setSeconds(0),this.date.setMilliseconds(0),Jd(this,a))}
function Id(a,b,c){b=new Date(a,b,c);0<=a&&100>a&&b.setFullYear(b.getFullYear()-1900);return b}
k=Hd.prototype;k.getFullYear=function(){return this.date.getFullYear()};
k.getMonth=function(){return this.date.getMonth()};
k.getDate=function(){return this.date.getDate()};
k.getTime=function(){return this.date.getTime()};
k.set=function(a){this.date=new Date(a.getFullYear(),a.getMonth(),a.getDate())};
k.add=function(a){if(a.f||a.b){var b=this.getMonth()+a.b+12*a.f,c=this.getFullYear()+Math.floor(b/12);b%=12;0>b&&(b+=12);a:{switch(b){case 1:var d=0!=c%4||0==c%100&&0!=c%400?28:29;break a;case 5:case 8:case 10:case 3:d=30;break a}d=31}d=Math.min(d,this.getDate());this.date.setDate(1);this.date.setFullYear(c);this.date.setMonth(b);this.date.setDate(d)}a.days&&(a=new Date((new Date(this.getFullYear(),this.getMonth(),this.getDate(),12)).getTime()+864E5*a.days),this.date.setDate(1),this.date.setFullYear(a.getFullYear()),
this.date.setMonth(a.getMonth()),this.date.setDate(a.getDate()),Jd(this,a.getDate()))};
k.U=function(a){return[this.getFullYear(),Ra(this.getMonth()+1),Ra(this.getDate())].join(a?"-":"")+""};
k.equals=function(a){return!(!a||this.getFullYear()!=a.getFullYear()||this.getMonth()!=a.getMonth()||this.getDate()!=a.getDate())};
k.toString=function(){return this.U()};
function Jd(a,b){a.getDate()!=b&&a.date.setUTCHours(a.date.getUTCHours()+(a.getDate()<b?1:-1))}
k.valueOf=function(){return this.date.valueOf()};
function Kd(a,b,c,d,e,f,g){this.date=la(a)?new Date(a,b||0,c||1,d||0,e||0,f||0,g||0):new Date(a&&a.getTime?a.getTime():Aa())}
y(Kd,Hd);Kd.prototype.add=function(a){Hd.prototype.add.call(this,a);a.hours&&this.date.setUTCHours(this.date.getUTCHours()+a.hours);a.minutes&&this.date.setUTCMinutes(this.date.getUTCMinutes()+a.minutes);a.seconds&&this.date.setUTCSeconds(this.date.getUTCSeconds()+a.seconds)};
Kd.prototype.U=function(a){var b=Hd.prototype.U.call(this,a);return a?b+" "+Ra(this.date.getHours())+":"+Ra(this.date.getMinutes())+":"+Ra(this.date.getSeconds()):b+"T"+Ra(this.date.getHours())+Ra(this.date.getMinutes())+Ra(this.date.getSeconds())};
Kd.prototype.equals=function(a){return this.getTime()==a.getTime()};
Kd.prototype.toString=function(){return this.U()};function Ld(){this.g=this.g;this.j=this.j}
Ld.prototype.g=!1;Ld.prototype.S=function(){return this.g};
Ld.prototype.dispose=function(){this.g||(this.g=!0,this.X())};
Ld.prototype.X=function(){if(this.j)for(;this.j.length;)this.j.shift()()};
function Md(a){a&&"function"==typeof a.dispose&&a.dispose()}
;function Nd(a){if(a.classList)return a.classList;a=a.className;return r(a)&&a.match(/\S+/g)||[]}
function K(a,b){return a.classList?a.classList.contains(b):Ia(Nd(a),b)}
function L(a,b){a.classList?a.classList.add(b):K(a,b)||(a.className+=0<a.className.length?" "+b:b)}
function Od(a,b){if(a.classList)A(b,function(b){L(a,b)});
else{var c={};A(Nd(a),function(a){c[a]=!0});
A(b,function(a){c[a]=!0});
a.className="";for(var d in c)a.className+=0<a.className.length?" "+d:d}}
function M(a,b){a.classList?a.classList.remove(b):K(a,b)&&(a.className=Ea(Nd(a),function(a){return a!=b}).join(" "))}
function Pd(a,b){a.classList?A(b,function(b){M(a,b)}):a.className=Ea(Nd(a),function(a){return!Ia(b,a)}).join(" ")}
function Qd(a,b,c){c?L(a,b):M(a,b)}
function Rd(a,b,c){K(a,b)&&(M(a,b),L(a,c))}
function Sd(a,b){var c=!K(a,b);Qd(a,b,c)}
;var Td=!C&&!eb();function Ud(a,b){if(/-[a-z]/.test(b))return null;if(Td&&a.dataset){if(gb()&&!(b in a.dataset))return null;var c=a.dataset[b];return void 0===c?null:c}return a.getAttribute("data-"+String(b).replace(/([A-Z])/g,"-$1").toLowerCase())}
;var Vd="StopIteration"in m?m.StopIteration:{message:"StopIteration",stack:""};function Wd(){}
Wd.prototype.next=function(){throw Vd;};
Wd.prototype.G=function(){return this};
function Xd(a){if(a instanceof Wd)return a;if("function"==typeof a.G)return a.G(!1);if(ra(a)){var b=0,c=new Wd;c.next=function(){for(;;){if(b>=a.length)throw Vd;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function Yd(a,b){if(ra(a))try{A(a,b,void 0)}catch(c){if(c!==Vd)throw c;}else{a=Xd(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==Vd)throw c;}}}
function Zd(a){if(ra(a))return Ka(a);a=Xd(a);var b=[];Yd(a,function(a){b.push(a)});
return b}
;function $d(a,b){this.g={};this.b=[];this.H=this.f=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof $d)for(c=ae(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function ae(a){be(a);return a.b.concat()}
k=$d.prototype;k.equals=function(a,b){if(this===a)return!0;if(this.f!=a.f)return!1;var c=b||ce;be(this);for(var d,e=0;d=this.b[e];e++)if(!c(this.get(d),a.get(d)))return!1;return!0};
function ce(a,b){return a===b}
k.isEmpty=function(){return 0==this.f};
k.clear=function(){this.g={};this.H=this.f=this.b.length=0};
k.remove=function(a){return Object.prototype.hasOwnProperty.call(this.g,a)?(delete this.g[a],this.f--,this.H++,this.b.length>2*this.f&&be(this),!0):!1};
function be(a){if(a.f!=a.b.length){for(var b=0,c=0;b<a.b.length;){var d=a.b[b];Object.prototype.hasOwnProperty.call(a.g,d)&&(a.b[c++]=d);b++}a.b.length=c}if(a.f!=a.b.length){var e={};for(c=b=0;b<a.b.length;)d=a.b[b],Object.prototype.hasOwnProperty.call(e,d)||(a.b[c++]=d,e[d]=1),b++;a.b.length=c}}
k.get=function(a,b){return Object.prototype.hasOwnProperty.call(this.g,a)?this.g[a]:b};
k.set=function(a,b){Object.prototype.hasOwnProperty.call(this.g,a)||(this.f++,this.b.push(a),this.H++);this.g[a]=b};
k.forEach=function(a,b){for(var c=ae(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
k.G=function(a){be(this);var b=0,c=this.H,d=this,e=new Wd;e.next=function(){if(c!=d.H)throw Error("The map has changed since the iterator was created");if(b>=d.b.length)throw Vd;var e=d.b[b++];return a?e:d.g[e]};
return e};function de(a){var b=[];ee(new fe,a,b);return b.join("")}
function fe(){}
function ee(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(qa(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),ee(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),ge(d,c),c.push(":"),ee(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":ge(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var he={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},ie=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function ge(a,b){b.push('"',a.replace(ie,function(a){var b=he[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),he[a]=b);return b}),'"')}
;function je(a,b,c,d){this.top=a;this.right=b;this.bottom=c;this.left=d}
je.prototype.getHeight=function(){return this.bottom-this.top};
je.prototype.ceil=function(){this.top=Math.ceil(this.top);this.right=Math.ceil(this.right);this.bottom=Math.ceil(this.bottom);this.left=Math.ceil(this.left);return this};
je.prototype.floor=function(){this.top=Math.floor(this.top);this.right=Math.floor(this.right);this.bottom=Math.floor(this.bottom);this.left=Math.floor(this.left);return this};
je.prototype.round=function(){this.top=Math.round(this.top);this.right=Math.round(this.right);this.bottom=Math.round(this.bottom);this.left=Math.round(this.left);return this};function ke(a,b,c,d){this.left=a;this.top=b;this.width=c;this.height=d}
ke.prototype.ceil=function(){this.left=Math.ceil(this.left);this.top=Math.ceil(this.top);this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
ke.prototype.floor=function(){this.left=Math.floor(this.left);this.top=Math.floor(this.top);this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
ke.prototype.round=function(){this.left=Math.round(this.left);this.top=Math.round(this.top);this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function le(a,b,c){if(r(b))(b=me(a,b))&&(a.style[b]=c);else for(var d in b){c=a;var e=b[d],f=me(c,d);f&&(c.style[f]=e)}}
var ne={};function me(a,b){var c=ne[b];if(!c){var d=Ua(b);c=d;void 0===a.style[d]&&(d=(qb?"Webkit":pb?"Moz":C?"ms":mb?"O":null)+Va(d),void 0!==a.style[d]&&(c=d));ne[b]=c}return c}
function oe(a,b){var c=Vb(a);return c.defaultView&&c.defaultView.getComputedStyle&&(c=c.defaultView.getComputedStyle(a,null))?c[b]||c.getPropertyValue(b)||"":""}
function pe(a,b){return oe(a,b)||(a.currentStyle?a.currentStyle[b]:null)||a.style&&a.style[b]}
function qe(a){try{var b=a.getBoundingClientRect()}catch(c){return{left:0,top:0,right:0,bottom:0}}C&&a.ownerDocument.body&&(a=a.ownerDocument,b.left-=a.documentElement.clientLeft+a.body.clientLeft,b.top-=a.documentElement.clientTop+a.body.clientTop);return b}
function re(a){if(C&&!(8<=Number(Fb)))return a.offsetParent;var b=Vb(a),c=pe(a,"position"),d="fixed"==c||"absolute"==c;for(a=a.parentNode;a&&a!=b;a=a.parentNode)if(11==a.nodeType&&a.host&&(a=a.host),c=pe(a,"position"),d=d&&"static"==c&&a!=b.documentElement&&a!=b.body,!d&&(a.scrollWidth>a.clientWidth||a.scrollHeight>a.clientHeight||"fixed"==c||"absolute"==c||"relative"==c))return a;return null}
function se(a){for(var b=new je(0,Infinity,Infinity,0),c=Tb(a),d=c.b.body,e=c.b.documentElement,f=cc(c.b);a=re(a);)if(!(C&&0==a.clientWidth||qb&&0==a.clientHeight&&a==d)&&a!=d&&a!=e&&"visible"!=pe(a,"overflow")){var g=te(a),h=new D(a.clientLeft,a.clientTop);g.x+=h.x;g.y+=h.y;b.top=Math.max(b.top,g.y);b.right=Math.min(b.right,g.x+a.clientWidth);b.bottom=Math.min(b.bottom,g.y+a.clientHeight);b.left=Math.max(b.left,g.x)}d=f.scrollLeft;f=f.scrollTop;b.left=Math.max(b.left,d);b.top=Math.max(b.top,f);c=
$b(dc(c.b)||window);b.right=Math.min(b.right,d+c.width);b.bottom=Math.min(b.bottom,f+c.height);return 0<=b.top&&0<=b.left&&b.bottom>b.top&&b.right>b.left?b:null}
function te(a){var b=Vb(a),c=new D(0,0);var d=b?Vb(b):document;d=!C||9<=Number(Fb)||ac(Tb(d).b)?d.documentElement:d.body;if(a==d)return c;a=qe(a);b=bc(Tb(b).b);c.x=a.left+b.x;c.y=a.top+b.y;return c}
function ue(a){a=qe(a);return new D(a.left,a.top)}
function ve(a,b){"number"==typeof a&&(a=(b?Math.round(a):a)+"px");return a}
function we(a){var b=xe;if("none"!=pe(a,"display"))return b(a);var c=a.style,d=c.display,e=c.visibility,f=c.position;c.visibility="hidden";c.position="absolute";c.display="inline";a=b(a);c.display=d;c.position=f;c.visibility=e;return a}
function xe(a){var b=a.offsetWidth,c=a.offsetHeight,d=qb&&!b&&!c;return p(b)&&!d||!a.getBoundingClientRect?new Sb(b,c):(a=qe(a),new Sb(a.right-a.left,a.bottom-a.top))}
function ye(a){var b=te(a);a=we(a);return new ke(b.x,b.y,a.width,a.height)}
function ze(a){return"rtl"==pe(a,"direction")}
function Ae(a,b){if(/^\d+px?$/.test(b))return parseInt(b,10);var c=a.style.left,d=a.runtimeStyle.left;a.runtimeStyle.left=a.currentStyle.left;a.style.left=b;var e=a.style.pixelLeft;a.style.left=c;a.runtimeStyle.left=d;return+e}
function Be(a,b){var c=a.currentStyle?a.currentStyle[b]:null;return c?Ae(a,c):0}
var Ce={thin:2,medium:4,thick:6};function De(a,b){if("none"==(a.currentStyle?a.currentStyle[b+"Style"]:null))return 0;var c=a.currentStyle?a.currentStyle[b+"Width"]:null;return c in Ce?Ce[c]:Ae(a,c)}
;var Ee=function(){if(sb){var a=/Windows NT ([0-9.]+)/;return(a=a.exec(Wa))?a[1]:"0"}return rb?(a=/10[_.][0-9_.]+/,(a=a.exec(Wa))?a[0].replace(/_/g,"."):"10"):tb?(a=/Android\s+([^\);]+)(\)|;)/,(a=a.exec(Wa))?a[1]:""):ub||vb||wb?(a=/(?:iPhone|CPU)\s+OS\s+(\S+)/,(a=a.exec(Wa))?a[1].replace(/_/g,"."):""):""}();function Fe(a){return(a=a.exec(Wa))?a[1]:""}
var Ge=function(){if(Bd)return Fe(/Firefox\/([0-9.]+)/);if(C||nb||mb)return Db;if(Fd)return ib()?Fe(/CriOS\/([0-9.]+)/):Fe(/Chrome\/([0-9.]+)/);if(Gd&&!ib())return Fe(/Version\/([0-9.]+)/);if(Cd||Dd){var a=/Version\/(\S+).*Mobile\/(\S+)/.exec(Wa);if(a)return a[1]+"."+a[2]}else if(Ed)return(a=Fe(/Android\s+([0-9.]+)/))?a:Fe(/Version\/([0-9.]+)/);return""}();function He(a,b,c,d,e,f,g){var h;if(h=c.offsetParent){var l="HTML"==h.tagName||"BODY"==h.tagName;if(!l||"static"!=pe(h,"position")){var n=te(h);if(!l){l=ze(h);var t;if(t=l){if(t=Gd)t=0<=Sa(Ge,10);var z;if(z=xb)z=0<=Sa(Ee,10);t=pb||t||z}l=t?-h.scrollLeft:!l||ob&&Eb("8")||"visible"==pe(h,"overflowX")?h.scrollLeft:h.scrollWidth-h.clientWidth-h.scrollLeft;n=Rb(n,new D(l,h.scrollTop))}}}h=n||new D;n=ye(a);if(l=se(a)){var q=new ke(l.left,l.top,l.right-l.left,l.bottom-l.top);l=Math.max(n.left,q.left);t=
Math.min(n.left+n.width,q.left+q.width);l<=t&&(z=Math.max(n.top,q.top),q=Math.min(n.top+n.height,q.top+q.height),z<=q&&(n.left=l,n.top=z,n.width=t-l,n.height=q-z))}l=Tb(a);z=Tb(c);if(l.b!=z.b){t=l.b.body;z=dc(z.b);q=new D(0,0);var I=(I=Vb(t))?dc(I):window;b:{try{jb(I.parent);var w=!0;break b}catch(zc){}w=!1}if(w){w=t;do{var na=I==z?te(w):ue(w);q.x+=na.x;q.y+=na.y}while(I&&I!=z&&I!=I.parent&&(w=I.frameElement)&&(I=I.parent))}w=Rb(q,te(t));!C||9<=Number(Fb)||ac(l.b)||(w=Rb(w,bc(l.b)));n.left+=w.x;n.top+=
w.y}a=Ie(a,b);b=n.left;a&4?b+=n.width:a&2&&(b+=n.width/2);b=new D(b,n.top+(a&1?n.height:0));b=Rb(b,h);e&&(b.x+=(a&4?-1:1)*e.x,b.y+=(a&1?-1:1)*e.y);var T;g&&(T=se(c))&&(T.top-=h.y,T.right-=h.x,T.bottom-=h.y,T.left-=h.x);return Je(b,c,d,f,T,g,void 0)}
function Je(a,b,c,d,e,f,g){a=new D(a.x,a.y);var h=Ie(b,c);c=we(b);g=g?new Sb(g.width,g.height):new Sb(c.width,c.height);a=new D(a.x,a.y);g=new Sb(g.width,g.height);var l=0;if(d||0!=h)h&4?a.x-=g.width+(d?d.right:0):h&2?a.x-=g.width/2:d&&(a.x+=d.left),h&1?a.y-=g.height+(d?d.bottom:0):d&&(a.y+=d.top);if(f){if(e){d=a;h=g;l=0;65==(f&65)&&(d.x<e.left||d.x>=e.right)&&(f&=-2);132==(f&132)&&(d.y<e.top||d.y>=e.bottom)&&(f&=-5);d.x<e.left&&f&1&&(d.x=e.left,l|=1);if(f&16){var n=d.x;d.x<e.left&&(d.x=e.left,l|=
4);d.x+h.width>e.right&&(h.width=Math.min(e.right-d.x,n+h.width-e.left),h.width=Math.max(h.width,0),l|=4)}d.x+h.width>e.right&&f&1&&(d.x=Math.max(e.right-h.width,e.left),l|=1);f&2&&(l|=(d.x<e.left?16:0)|(d.x+h.width>e.right?32:0));d.y<e.top&&f&4&&(d.y=e.top,l|=2);f&32&&(n=d.y,d.y<e.top&&(d.y=e.top,l|=8),d.y+h.height>e.bottom&&(h.height=Math.min(e.bottom-d.y,n+h.height-e.top),h.height=Math.max(h.height,0),l|=8));d.y+h.height>e.bottom&&f&4&&(d.y=Math.max(e.bottom-h.height,e.top),l|=2);f&8&&(l|=(d.y<
e.top?64:0)|(d.y+h.height>e.bottom?128:0));e=l}else e=256;l=e}f=new ke(0,0,0,0);f.left=a.x;f.top=a.y;f.width=g.width;f.height=g.height;e=l;if(e&496)return e;g=new D(f.left,f.top);g instanceof D?(a=g.x,g=g.y):(a=g,g=void 0);b.style.left=ve(a,!1);b.style.top=ve(g,!1);g=new Sb(f.width,f.height);c==g||c&&g&&c.width==g.width&&c.height==g.height||(c=g,g=ac(Tb(Vb(b)).b),!C||Eb("10")||g&&Eb("8")?(b=b.style,pb?b.MozBoxSizing="border-box":qb?b.WebkitBoxSizing="border-box":b.boxSizing="border-box",b.width=Math.max(c.width,
0)+"px",b.height=Math.max(c.height,0)+"px"):(a=b.style,g?(C?(g=Be(b,"paddingLeft"),f=Be(b,"paddingRight"),d=Be(b,"paddingTop"),h=Be(b,"paddingBottom"),g=new je(d,f,h,g)):(g=oe(b,"paddingLeft"),f=oe(b,"paddingRight"),d=oe(b,"paddingTop"),h=oe(b,"paddingBottom"),g=new je(parseFloat(d),parseFloat(f),parseFloat(h),parseFloat(g))),!C||9<=Number(Fb)?(f=oe(b,"borderLeftWidth"),d=oe(b,"borderRightWidth"),h=oe(b,"borderTopWidth"),b=oe(b,"borderBottomWidth"),b=new je(parseFloat(h),parseFloat(d),parseFloat(b),
parseFloat(f))):(f=De(b,"borderLeft"),d=De(b,"borderRight"),h=De(b,"borderTop"),b=De(b,"borderBottom"),b=new je(h,d,b,f)),a.pixelWidth=c.width-b.left-g.left-g.right-b.right,a.pixelHeight=c.height-b.top-g.top-g.bottom-b.bottom):(a.pixelWidth=c.width,a.pixelHeight=c.height)));return e}
function Ie(a,b){return(b&8&&ze(a)?b^4:b)&-9}
;function Ke(a){this.b=0;this.A=void 0;this.j=this.f=this.g=null;this.l=this.o=!1;if(a!=ma)try{var b=this;a.call(void 0,function(a){Le(b,2,a)},function(a){Le(b,3,a)})}catch(c){Le(this,3,c)}}
function Me(){this.next=this.context=this.onRejected=this.f=this.b=null;this.g=!1}
Me.prototype.reset=function(){this.context=this.onRejected=this.f=this.b=null;this.g=!1};
var Ne=new nd(function(){return new Me},function(a){a.reset()});
function Oe(a,b,c){var d=Ne.get();d.f=a;d.onRejected=b;d.context=c;return d}
Ke.prototype.then=function(a,b,c){return Pe(this,sa(a)?a:null,sa(b)?b:null,c)};
Ke.prototype.then=Ke.prototype.then;Ke.prototype.$goog_Thenable=!0;Ke.prototype.cancel=function(a){0==this.b&&vd(function(){var b=new Qe(a);Re(this,b)},this)};
function Re(a,b){if(0==a.b)if(a.g){var c=a.g;if(c.f){for(var d=0,e=null,f=null,g=c.f;g&&(g.g||(d++,g.b==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.b&&1==d?Re(c,b):(f?(d=f,d.next==c.j&&(c.j=d),d.next=d.next.next):Se(c),Te(c,e,3,b)))}a.g=null}else Le(a,3,b)}
function Ue(a,b){a.f||2!=a.b&&3!=a.b||Ve(a);a.j?a.j.next=b:a.f=b;a.j=b}
function Pe(a,b,c,d){var e=Oe(null,null,null);e.b=new Ke(function(a,g){e.f=b?function(c){try{var e=b.call(d,c);a(e)}catch(n){g(n)}}:a;
e.onRejected=c?function(b){try{var e=c.call(d,b);!p(e)&&b instanceof Qe?g(b):a(e)}catch(n){g(n)}}:g});
e.b.g=a;Ue(a,e);return e.b}
Ke.prototype.J=function(a){this.b=0;Le(this,2,a)};
Ke.prototype.P=function(a){this.b=0;Le(this,3,a)};
function Le(a,b,c){if(0==a.b){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.b=1;a:{var d=c,e=a.J,f=a.P;if(d instanceof Ke){Ue(d,Oe(e||ma,f||null,a));var g=!0}else{if(d)try{var h=!!d.$goog_Thenable}catch(n){h=!1}else h=!1;if(h)d.then(e,f,a),g=!0;else{if(ta(d))try{var l=d.then;if(sa(l)){We(d,l,e,f,a);g=!0;break a}}catch(n){f.call(a,n);g=!0;break a}g=!1}}}g||(a.A=c,a.b=b,a.g=null,Ve(a),3!=b||c instanceof Qe||Xe(a,c))}}
function We(a,b,c,d,e){function f(a){h||(h=!0,d.call(e,a))}
function g(a){h||(h=!0,c.call(e,a))}
var h=!1;try{b.call(a,g,f)}catch(l){f(l)}}
function Ve(a){a.o||(a.o=!0,vd(a.C,a))}
function Se(a){var b=null;a.f&&(b=a.f,a.f=b.next,b.next=null);a.f||(a.j=null);return b}
Ke.prototype.C=function(){for(var a;a=Se(this);)Te(this,a,this.b,this.A);this.o=!1};
function Te(a,b,c,d){if(3==c&&b.onRejected&&!b.g)for(;a&&a.l;a=a.g)a.l=!1;if(b.b)b.b.g=null,Ye(b,c,d);else try{b.g?b.f.call(b.context):Ye(b,c,d)}catch(e){Ze.call(null,e)}od(Ne,b)}
function Ye(a,b,c){2==b?a.f.call(a.context,c):a.onRejected&&a.onRejected.call(a.context,c)}
function Xe(a,b){a.l=!0;vd(function(){a.l&&Ze.call(null,b)})}
var Ze=pd;function Qe(a){Ba.call(this,a)}
y(Qe,Ba);Qe.prototype.name="cancel";function N(a){Ld.call(this);this.A=1;this.l=[];this.o=0;this.b=[];this.f={};this.C=!!a}
y(N,Ld);k=N.prototype;k.subscribe=function(a,b,c){var d=this.f[a];d||(d=this.f[a]=[]);var e=this.A;this.b[e]=a;this.b[e+1]=b;this.b[e+2]=c;this.A=e+3;d.push(e);return e};
function $e(a,b){var c=!1,d=a.subscribe("ROOT_MENU_REMOVED",function(a){c||(c=!0,this.O(d),b.apply(void 0,arguments))},a)}
function af(a,b,c){if(b=a.f[b]){var d=a.b;(b=Ha(b,function(a){return d[a+1]==c&&void 0==d[a+2]}))&&a.O(b)}}
k.O=function(a){var b=this.b[a];if(b){var c=this.f[b];if(0!=this.o)this.l.push(a),this.b[a+1]=ma;else{if(c){var d=Da(c,a);0<=d&&Array.prototype.splice.call(c,d,1)}delete this.b[a];delete this.b[a+1];delete this.b[a+2]}}return!!b};
k.F=function(a,b){var c=this.f[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.C)for(e=0;e<c.length;e++){var g=c[e];bf(this.b[g+1],this.b[g+2],d)}else{this.o++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.b[g+1].apply(this.b[g+2],d)}finally{if(this.o--,0<this.l.length&&0==this.o)for(;c=this.l.pop();)this.O(c)}}return 0!=e}return!1};
function bf(a,b,c){vd(function(){a.apply(b,c)})}
k.clear=function(a){if(a){var b=this.f[a];b&&(A(b,this.O,this),delete this.f[a])}else this.b.length=0,this.f={}};
function cf(a,b){if(b){var c=a.f[b];return c?c.length:0}c=0;for(var d in a.f)c+=cf(a,d);return c}
k.X=function(){N.w.X.call(this);this.clear();this.l.length=0};function df(a){this.b=a}
df.prototype.set=function(a,b){p(b)?this.b.set(a,de(b)):this.b.remove(a)};
df.prototype.get=function(a){try{var b=this.b.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
df.prototype.remove=function(a){this.b.remove(a)};function ef(a){this.b=a}
y(ef,df);function ff(a){this.data=a}
function gf(a){return!p(a)||a instanceof ff?a:new ff(a)}
ef.prototype.set=function(a,b){ef.w.set.call(this,a,gf(b))};
ef.prototype.f=function(a){a=ef.w.get.call(this,a);if(!p(a)||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
ef.prototype.get=function(a){if(a=this.f(a)){if(a=a.data,!p(a))throw"Storage: Invalid value was encountered";}else a=void 0;return a};function hf(a){this.b=a}
y(hf,ef);hf.prototype.set=function(a,b,c){if(b=gf(b)){if(c){if(c<Aa()){hf.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Aa()}hf.w.set.call(this,a,b)};
hf.prototype.f=function(a){var b=hf.w.f.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Aa()||c&&c>Aa())hf.prototype.remove.call(this,a);else return b}};function jf(){}
;function kf(){}
y(kf,jf);kf.prototype.clear=function(){var a=Zd(this.G(!0)),b=this;A(a,function(a){b.remove(a)})};function lf(a){this.b=a}
y(lf,kf);k=lf.prototype;k.isAvailable=function(){if(!this.b)return!1;try{return this.b.setItem("__sak","1"),this.b.removeItem("__sak"),!0}catch(a){return!1}};
k.set=function(a,b){try{this.b.setItem(a,b)}catch(c){if(0==this.b.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
k.get=function(a){a=this.b.getItem(a);if(!r(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
k.remove=function(a){this.b.removeItem(a)};
k.G=function(a){var b=0,c=this.b,d=new Wd;d.next=function(){if(b>=c.length)throw Vd;var d=c.key(b++);if(a)return d;d=c.getItem(d);if(!r(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
k.clear=function(){this.b.clear()};
k.key=function(a){return this.b.key(a)};function mf(){var a=null;try{a=window.localStorage||null}catch(b){}this.b=a}
y(mf,lf);function nf(a,b){this.f=a;this.b=null;if(C&&!(9<=Number(Fb))){of||(of=new $d);this.b=of.get(a);this.b||(b?this.b=document.getElementById(b):(this.b=document.createElement("userdata"),this.b.addBehavior("#default#userData"),document.body.appendChild(this.b)),of.set(a,this.b));try{this.b.load(this.f)}catch(c){this.b=null}}}
y(nf,kf);var pf={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},of=null;function qf(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(a){return pf[a]})}
k=nf.prototype;k.isAvailable=function(){return!!this.b};
k.set=function(a,b){this.b.setAttribute(qf(a),b);rf(this)};
k.get=function(a){a=this.b.getAttribute(qf(a));if(!r(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
k.remove=function(a){this.b.removeAttribute(qf(a));rf(this)};
k.G=function(a){var b=0,c=this.b.XMLDocument.documentElement.attributes,d=new Wd;d.next=function(){if(b>=c.length)throw Vd;var d=c[b++];if(a)return decodeURIComponent(d.nodeName.replace(/\./g,"%")).substr(1);d=d.nodeValue;if(!r(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
k.clear=function(){for(var a=this.b.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);rf(this)};
function rf(a){try{a.b.save(a.f)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function sf(a,b){this.f=a;this.b=b+"::"}
y(sf,kf);sf.prototype.set=function(a,b){this.f.set(this.b+a,b)};
sf.prototype.get=function(a){return this.f.get(this.b+a)};
sf.prototype.remove=function(a){this.f.remove(this.b+a)};
sf.prototype.G=function(a){var b=this.f.G(!0),c=this,d=new Wd;d.next=function(){for(var d=b.next();d.substr(0,c.b.length)!=c.b;)d=b.next();return a?d.substr(c.b.length):c.f.get(d)};
return d};var tf=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function uf(a){return a?decodeURI(a):a}
function vf(a,b){if(!b)return a;var c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);c=[a.substr(0,d),e,a.substr(c)];d=c[1];c[1]=b?d?d+"&"+b:b:d;return c[0]+(c[1]?"?"+c[1]:"")+c[2]}
function wf(a,b,c){if(qa(b))for(var d=0;d<b.length;d++)wf(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function xf(a,b){for(var c=[],d=b||0;d<a.length;d+=2)wf(a[d],a[d+1],c);return c.join("&")}
function yf(a){var b=[],c;for(c in a)wf(c,a[c],b);return b.join("&")}
function zf(a,b){var c=2==arguments.length?xf(arguments[1],0):xf(arguments,1);return vf(a,c)}
function Af(a,b){var c=yf(b);return vf(a,c)}
;var Bf=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};x("yt.config_",Bf);function Cf(a){var b=arguments;if(1<b.length)Bf[b[0]]=b[1];else{b=b[0];for(var c in b)Bf[c]=b[c]}}
function O(a,b){return a in Bf?Bf[a]:b}
;function Df(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Ef(b)}}:a}
function Ef(a){var b=u("yt.logging.errors.log");b?b(a,void 0,void 0,void 0,void 0):(b=O("ERRORS",[]),b.push([a,void 0,void 0,void 0,void 0]),Cf("ERRORS",b))}
;function P(a,b){sa(a)&&(a=Df(a));return window.setTimeout(a,b)}
;var Ff=u("ytPubsubPubsubInstance")||new N;N.prototype.subscribe=N.prototype.subscribe;N.prototype.unsubscribeByKey=N.prototype.O;N.prototype.publish=N.prototype.F;N.prototype.clear=N.prototype.clear;x("ytPubsubPubsubInstance",Ff);var Gf=u("ytPubsubPubsubSubscribedKeys")||{};x("ytPubsubPubsubSubscribedKeys",Gf);var Hf=u("ytPubsubPubsubTopicToKeys")||{};x("ytPubsubPubsubTopicToKeys",Hf);var If=u("ytPubsubPubsubIsSynchronous")||{};x("ytPubsubPubsubIsSynchronous",If);
function Jf(a,b,c){var d=Kf();if(d){var e=d.subscribe(a,function(){var d=arguments;var g=function(){Gf[e]&&b.apply(c||window,d)};
try{If[a]?g():P(g,0)}catch(h){Ef(h)}},c);
Gf[e]=!0;Hf[a]||(Hf[a]=[]);Hf[a].push(e);return e}return 0}
function Lf(a){var b=Kf();b&&(la(a)?a=[a]:r(a)&&(a=[parseInt(a,10)]),A(a,function(a){b.unsubscribeByKey(a);delete Gf[a]}))}
function Q(a,b){var c=Kf();return c?c.publish.apply(c,arguments):!1}
function Mf(a,b){If[a]=!0;var c=Kf();c&&c.publish.apply(c,arguments);If[a]=!1}
function Kf(){return u("ytPubsubPubsubInstance")}
;function Nf(a,b,c){a&&(a.dataset?a.dataset[Of(b)]=String(c):a.setAttribute("data-"+b,c))}
function Pf(a,b){return a?a.dataset?a.dataset[Of(b)]:a.getAttribute("data-"+b):null}
function Qf(a,b){a&&(a.dataset?delete a.dataset[Of(b)]:a.removeAttribute("data-"+b))}
var Rf={};function Of(a){return Rf[a]||(Rf[a]=String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()}))}
;function R(a,b){this.version=a;this.args=b}
;function S(a,b){this.topic=a;this.b=b}
S.prototype.toString=function(){return this.topic};function Sf(a){var b=void 0;isNaN(b)&&(b=void 0);var c=u("yt.scheduler.instance.addJob");c?c(a,1,b):void 0===b?a():P(a,b||0)}
;function Tf(){}
function Uf(){}
Tf.prototype=aa(Uf.prototype);Tf.prototype.constructor=Tf;if(fa)fa(Tf,Uf);else for(var Vf in Uf)if("prototype"!=Vf)if(Object.defineProperties){var Wf=Object.getOwnPropertyDescriptor(Uf,Vf);Wf&&Object.defineProperty(Tf,Vf,Wf)}else Tf[Vf]=Uf[Vf];Tf.w=Uf.prototype;Tf.prototype.start=function(){var a=u("yt.scheduler.instance.start");a&&a()};
oa(Tf);Tf.v();var Xf=u("ytPubsub2Pubsub2Instance")||new N;N.prototype.subscribe=N.prototype.subscribe;N.prototype.unsubscribeByKey=N.prototype.O;N.prototype.publish=N.prototype.F;N.prototype.clear=N.prototype.clear;x("ytPubsub2Pubsub2Instance",Xf);var Yf=u("ytPubsub2Pubsub2SubscribedKeys")||{};x("ytPubsub2Pubsub2SubscribedKeys",Yf);var Zf=u("ytPubsub2Pubsub2TopicToKeys")||{};x("ytPubsub2Pubsub2TopicToKeys",Zf);var $f=u("ytPubsub2Pubsub2IsAsync")||{};x("ytPubsub2Pubsub2IsAsync",$f);
x("ytPubsub2Pubsub2SkipSubKey",null);function U(a,b){var c=ag();c&&c.publish.call(c,a.toString(),a,b)}
function bg(a,b,c){var d=ag();if(!d)return 0;var e=d.subscribe(a.toString(),function(d,g){var f=u("ytPubsub2Pubsub2SkipSubKey");f&&f==e||(f=function(){if(Yf[e])try{if(g&&a instanceof S&&a!=d)try{var f=a.b,h=g;if(!h.args||!h.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!f.H){var t=new f;f.H=t.version}var z=f.H}catch(q){}if(!z||h.version!=z)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{g=Reflect.construct(f,Ka(h.args))}catch(q){throw q.message=
"yt.pubsub2.Data.deserialize(): "+q.message,q;}}catch(q){throw q.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+a.toString()+": "+q.message,q;}b.call(c||window,g)}catch(q){Ef(q)}},$f[a.toString()]?u("yt.scheduler.instance")?Sf(f):P(f,0):f())});
Yf[e]=!0;Zf[a.toString()]||(Zf[a.toString()]=[]);Zf[a.toString()].push(e);return e}
function cg(a){var b=ag();b&&(la(a)&&(a=[a]),A(a,function(a){b.unsubscribeByKey(a);delete Yf[a]}))}
function ag(){return u("ytPubsub2Pubsub2Instance")}
;var dg=0;function eg(a){var b=a.__yt_uid_key;b||(b=fg(),a.__yt_uid_key=b);return b}
function gg(a,b){a=E(a);b=E(b);return!!tc(a,function(a){return a===b},!0,void 0)}
function hg(a,b){var c=Xb(document,a,null,b);return c.length?c[0]:null}
function ig(){var a=document,b;Ga(["fullscreenElement","webkitFullscreenElement","mozFullScreenElement","msFullscreenElement"],function(c){b=a[c];return!!b});
return b}
function jg(){Qd(document.body,"hide-players",!1);A(Wb("preserve-players"),function(a){M(a,"preserve-players")})}
var fg=u("ytDomDomGetNextId")||function(){return++dg};
x("ytDomDomGetNextId",fg);var kg={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function lg(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;if(a=a||window.event){this.event=a;for(var b in a)b in kg||(this[b]=a[b]);(b=a.target||a.srcElement)&&3==b.nodeType&&(b=b.parentNode);this.target=b;if(b=a.relatedTarget)try{b=b.nodeName?b:null}catch(c){b=null}else"mouseover"==this.type?
b=a.fromElement:"mouseout"==this.type&&(b=a.toElement);this.relatedTarget=b;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey}}
lg.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
lg.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
lg.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var bb=u("ytEventsEventsListeners")||{};x("ytEventsEventsListeners",bb);var mg=u("ytEventsEventsCounter")||{count:0};x("ytEventsEventsCounter",mg);
function ng(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return ab(function(e){var f="boolean"==typeof e[4]&&e[4]==!!d,g;if(g=ta(e[4])&&ta(d))a:{g=e[4];for(var h in g)if(!(h in d)||g[h]!==d[h]){g=!1;break a}for(h in d)if(!(h in g)){g=!1;break a}g=!0}return!!e.length&&e[0]==a&&e[1]==b&&e[2]==
c&&(f||g)})}
function V(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=ng(a,b,c,d);if(e)return e;e=++mg.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(d){d=new lg(d);if(!tc(d.relatedTarget,function(b){return b==a},!0))return d.currentTarget=a,d.type=b,c.call(a,d)}:function(b){b=new lg(b);
b.currentTarget=a;return c.call(a,b)};
g=Df(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),og()||"boolean"==typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);bb[e]=[a,b,c,g,d];return e}
function pg(a,b,c){var d=a||document;return V(d,"click",function(a){var e=tc(a.target,function(a){return a===d||c(a)},!0);
e&&e!==d&&!e.disabled&&(a.currentTarget=e,b.call(e,a))})}
function qg(a){a=a||window.event;a=a.target||a.srcElement;3==a.nodeType&&(a=a.parentNode);return a}
var og=function(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}(function(){var a=!1;
try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function rg(a,b,c){return pg(a,b,function(a){return K(a,c)})}
function sg(a){if(document.createEvent){var b=document.createEvent("HTMLEvents");b.initEvent("click",!0,!0);a.dispatchEvent(b)}else b=document.createEventObject(),a.fireEvent("onclick",b)}
function W(a){a&&("string"==typeof a&&(a=[a]),A(a,function(a){if(a in bb){var b=bb[a],d=b[0],e=b[1],f=b[3];b=b[4];d.removeEventListener?og()||"boolean"==typeof b?d.removeEventListener(e,f,b):d.removeEventListener(e,f,!!b.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete bb[a]}}))}
;var tg={},ug="ontouchstart"in document;function vg(a,b,c){switch(a){case "mouseover":case "mouseout":var d=3;break;case "mouseenter":case "mouseleave":d=9}return tc(c,function(a){return K(a,b)},!0,d)}
function wg(a){var b="mouseover"==a.type&&"mouseenter"in tg||"mouseout"==a.type&&"mouseleave"in tg,c=a.type in tg||b;if("HTML"!=a.target.tagName&&c){if(b){b="mouseover"==a.type?"mouseenter":"mouseleave";c=tg[b];for(var d in c.f){var e=vg(b,d,a.target);e&&!tc(a.relatedTarget,function(a){return a==e},!0)&&c.F(d,e,b,a)}}if(b=tg[a.type])for(d in b.f)(e=vg(a.type,d,a.target))&&b.F(d,e,a.type,a)}}
V(document,"blur",wg,!0);V(document,"change",wg,!0);V(document,"click",wg);V(document,"focus",wg,!0);V(document,"mouseover",wg);V(document,"mouseout",wg);V(document,"mousedown",wg);V(document,"keydown",wg);V(document,"keyup",wg);V(document,"keypress",wg);V(document,"cut",wg);V(document,"paste",wg);ug&&(V(document,"touchstart",wg),V(document,"touchend",wg),V(document,"touchcancel",wg));function xg(a){this.l=a;this.A={};this.J=[];this.C=[]}
k=xg.prototype;k.B=function(a){return G(a,X(this))};
function X(a,b){return"yt-uix"+(a.l?"-"+a.l:"")+(b?"-"+b:"")}
k.unregister=function(){Lf(this.J);this.J.length=0;cg(this.C);this.C.length=0};
k.init=ma;k.dispose=ma;function yg(a,b,c){a.J.push(Jf(b,c,a))}
function zg(a,b,c){a.C.push(bg(b,c,a))}
function Y(a,b,c,d){d=X(a,d);var e=v(c,a);b in tg||(tg[b]=new N);tg[b].subscribe(d,e);a.A[c]=e}
function Z(a,b,c,d){if(b in tg){var e=tg[b];af(e,X(a,d),a.A[c]);0>=cf(e)&&(e.dispose(),delete tg[b])}delete a.A[c]}
k.N=function(a,b,c){var d=this.i(a,b);if(d&&(d=u(d))){var e=Na(arguments,2);Ma(e,0,0,a);d.apply(null,e)}};
k.i=function(a,b){return Pf(a,b)};
function Ag(a,b){Nf(a,"tooltip-text",b)}
;var Bg=window.yt&&window.yt.uix&&window.yt.uix.widgets_||{};x("yt.uix.widgets_",Bg);function Cg(a){"?"==a.charAt(0)&&(a=a.substr(1));a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length){var f=decodeURIComponent((e[0]||"").replace(/\+/g," "));e=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?qa(b[f])?La(b[f],e):b[f]=[b[f],e]:b[f]=e}}return b}
;function Dg(a){a=void 0===a?{}:a;sa(a)&&(a={callback:a});if(a.gapiHintOverride||O("GAPI_HINT_OVERRIDE")){var b=document.location.href;-1!=b.indexOf("?")?(b=(b||"").split("#")[0],b=b.split("?",2),b=Cg(1<b.length?b[1]:b[0])):b={};(b=b.gapi_jsh)&&db(a,{_c:{jsl:{h:b}}})}ld("gapi.iframes:gapi.iframes.style.common",a)}
;function Eg(){return u("gapi.iframes.getContext")()}
;function Fg(a){R.call(this,1,arguments);this.b=a}
y(Fg,R);function Gg(a){R.call(this,1,arguments);this.b=a}
y(Gg,R);function Hg(a,b,c){R.call(this,3,arguments);this.g=a;this.f=b;this.b=null!=c?!!c:null}
y(Hg,R);function Ig(a,b,c,d,e){R.call(this,2,arguments);this.f=a;this.b=b;this.j=c||null;this.g=d||null;this.source=e||null}
y(Ig,R);function Jg(a,b,c){R.call(this,1,arguments);this.b=a;this.f=b}
y(Jg,R);function Kg(a,b,c,d,e,f,g){R.call(this,1,arguments);this.f=a;this.l=b;this.b=c;this.o=d||null;this.j=e||null;this.g=f||null;this.source=g||null}
y(Kg,R);
var Lg=new S("subscription-batch-subscribe",Fg),Mg=new S("subscription-batch-unsubscribe",Fg),Ng=new S("subscription-subscribe",Ig),Og=new S("subscription-subscribe-loading",Gg),Pg=new S("subscription-subscribe-loaded",Gg),Qg=new S("subscription-subscribe-success",Jg),Rg=new S("subscription-subscribe-external",Ig),Sg=new S("subscription-unsubscribe",Kg),Tg=new S("subscription-unsubscirbe-loading",Gg),Ug=new S("subscription-unsubscribe-loaded",Gg),Vg=new S("subscription-unsubscribe-success",Gg),Wg=
new S("subscription-external-unsubscribe",Kg),Xg=new S("subscription-enable-ypc",Gg),Yg=new S("subscription-disable-ypc",Gg),Zg=new S("subscription-prefs",Hg),$g=new S("subscription-prefs-success",Hg),ah=new S("subscription-prefs-failure",Hg);function bh(){var a=ig();return a?a:null}
;function ch(a,b){(a=E(a))&&a.style&&(a.style.display=b?"":"none",Qd(a,"hid",!b))}
function dh(a){return(a=E(a))?"none"!=a.style.display&&!K(a,"hid"):!1}
function eh(a){A(arguments,function(a){!ra(a)||a instanceof Element?ch(a,!0):A(a,function(a){eh(a)})})}
function fh(a){A(arguments,function(a){!ra(a)||a instanceof Element?ch(a,!1):A(a,function(a){fh(a)})})}
;function gh(){xg.call(this,"tooltip");this.b=0;this.f={}}
y(gh,xg);oa(gh);k=gh.prototype;k.register=function(){Y(this,"mouseover",this.T);Y(this,"mouseout",this.K);Y(this,"focus",this.pa);Y(this,"blur",this.ka);Y(this,"click",this.K);Y(this,"touchstart",this.Ga);Y(this,"touchend",this.V);Y(this,"touchcancel",this.V)};
k.unregister=function(){Z(this,"mouseover",this.T);Z(this,"mouseout",this.K);Z(this,"focus",this.pa);Z(this,"blur",this.ka);Z(this,"click",this.K);Z(this,"touchstart",this.Ga);Z(this,"touchend",this.V);Z(this,"touchcancel",this.V);this.dispose();gh.w.unregister.call(this)};
k.dispose=function(){for(var a in this.f)this.K(this.f[a]);this.f={}};
k.T=function(a){if(!(this.b&&1E3>Aa()-this.b)){var b=parseInt(this.i(a,"tooltip-hide-timer"),10);b&&(Qf(a,"tooltip-hide-timer"),window.clearTimeout(b));b=v(function(){hh(this,a);Qf(a,"tooltip-show-timer")},this);
var c=parseInt(this.i(a,"tooltip-show-delay"),10)||0;b=P(b,c);Nf(a,"tooltip-show-timer",b.toString());a.title&&(Ag(a,ih(this,a)),a.title="");b=ua(a).toString();this.f[b]=a}};
k.K=function(a){var b=parseInt(this.i(a,"tooltip-show-timer"),10);b&&(window.clearTimeout(b),Qf(a,"tooltip-show-timer"));b=v(function(){if(a){var b=E(jh(this,a));b&&(kh(b),ec(b),Qf(a,"content-id"));b=E(jh(this,a,"arialabel"));ec(b)}Qf(a,"tooltip-hide-timer")},this);
b=P(b,50);Nf(a,"tooltip-hide-timer",b.toString());if(b=this.i(a,"tooltip-text"))a.title=b;b=ua(a).toString();delete this.f[b]};
k.pa=function(a,b){this.b=0;this.T(a,b)};
k.ka=function(a){this.b=0;this.K(a)};
k.Ga=function(a,b,c){c.changedTouches&&(this.b=0,(a=vg(b,X(this),c.changedTouches[0].target))&&this.T(a,b))};
k.V=function(a,b,c){c.changedTouches&&(this.b=Aa(),(a=vg(b,X(this),c.changedTouches[0].target))&&this.K(a))};
function lh(a,b,c){Ag(b,c);a=a.i(b,"content-id");(a=E(a))&&ic(a,c)}
function ih(a,b){return a.i(b,"tooltip-text")||b.title}
function hh(a,b){if(b){var c=ih(a,b);if(c){var d=E(jh(a,b));if(!d){d=document.createElement("div");d.id=jh(a,b);d.className=X(a,"tip");var e=document.createElement("div");e.className=X(a,"tip-body");var f=document.createElement("div");f.className=X(a,"tip-arrow");var g=document.createElement("div");g.setAttribute("aria-hidden","true");g.className=X(a,"tip-content");var h=mh(a,b),l=jh(a,b,"content");g.id=l;Nf(b,"content-id",l);e.appendChild(g);h&&d.appendChild(h);d.appendChild(e);d.appendChild(f);
var n=qc(b);l=jh(a,b,"arialabel");f=document.createElement("div");L(f,X(a,"arialabel"));f.id=l;n=b.hasAttribute("aria-label")?b.getAttribute("aria-label"):"rtl"==document.body.getAttribute("dir")?c+" "+n:n+" "+c;ic(f,n);b.setAttribute("aria-labelledby",l);l=bh()||document.body;l.appendChild(f);l.appendChild(d);lh(a,b,c);(c=parseInt(a.i(b,"tooltip-max-width"),10))&&e.offsetWidth>c&&(e.style.width=c+"px",L(g,X(a,"normal-wrap")));g=K(b,X(a,"reverse"));nh(a,b,d,e,h,g)||nh(a,b,d,e,h,!g);var t=X(a,"tip-visible");
P(function(){L(d,t)},0)}}}}
function nh(a,b,c,d,e,f){Qd(c,X(a,"tip-reverse"),f);var g=0;f&&(g=1);var h=we(b);f=new D((h.width-10)/2,f?h.height:0);var l=te(b);Je(new D(l.x+f.x,l.y+f.y),c,g);f=$b(window);if(1==c.nodeType)var n=ue(c);else c=c.changedTouches?c.changedTouches[0]:c,n=new D(c.clientX,c.clientY);c=we(d);var t=Math.floor(c.width/2);g=!!(f.height<n.y+h.height);h=!!(n.y<h.height);l=!!(n.x<t);f=!!(f.width<n.x+t);n=(c.width+3)/-2- -5;a=a.i(b,"force-tooltip-direction");if("left"==a||l)n=-5;else if("right"==a||f)n=20-c.width-
3;a=Math.floor(n)+"px";d.style.left=a;e&&(e.style.left=a,e.style.height=c.height+"px",e.style.width=c.width+"px");return!(g||h)}
function jh(a,b,c){a=X(a)+eg(b);c&&(a+="-"+c);return a}
function mh(a,b){var c=null;sb&&K(b,X(a,"masked"))&&((c=E("yt-uix-tooltip-shared-mask"))?(c.parentNode.removeChild(c),eh(c)):(c=document.createElement("IFRAME"),c.src='javascript:""',c.id="yt-uix-tooltip-shared-mask",c.className=X(a,"tip-mask")));return c}
function kh(a){var b=E("yt-uix-tooltip-shared-mask"),c=b&&tc(b,function(b){return b==a},!1,2);
b&&c&&(b.parentNode.removeChild(b),fh(b),document.body.appendChild(b))}
;function oh(a){var b=ph();if(b=window.open(b,"loginPopup","width=375,height=440,resizable=yes,scrollbars=yes",!0)){var c=Jf("LOGGED_IN",function(b){Lf(O("LOGGED_IN_PUBSUB_KEY",void 0));Cf("LOGGED_IN",!0);a(b)});
Cf("LOGGED_IN_PUBSUB_KEY",c);b.moveTo((screen.width-375)/2,(screen.height-440)/2)}}
function ph(){var a=document.location.protocol+"//"+document.domain+"/post_login";a=zf(a,"mode","subscribe");a=zf("/signin?context=popup","next",a);return a=zf(a,"feature","sub_button")}
x("yt.pubsub.publish",Q);var qh=Object.create(null);qh.log_event="GENERIC_EVENT_LOGGING";qh.log_interaction="INTERACTION_LOGGING";x("ytLoggingTransportLogPayloadsQueue_",u("ytLoggingTransportLogPayloadsQueue_")||{});x("ytLoggingTransportTokensToCttTargetIds_",u("ytLoggingTransportTokensToCttTargetIds_")||{});x("ytLoggingTransportDispatchedStats_",u("ytLoggingTransportDispatchedStats_")||{});x("ytytLoggingTransportCapturedTime_",u("ytLoggingTransportCapturedTime_")||{});Aa();var rh=p(XMLHttpRequest)?function(){return new XMLHttpRequest}:p(ActiveXObject)?function(){return new ActiveXObject("Microsoft.XMLHTTP")}:null;
function sh(){if(!rh)return null;var a=rh();return"open"in a?a:null}
;var th={"X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},uh=!1;
function vh(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=a.match(tf)[1]||null,e=uf(a.match(tf)[3]||null);d&&e?(d=c,c=a.match(tf),d=d.match(tf),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?uf(c.match(tf)[3]||null)==e&&(Number(c.match(tf)[4]||null)||null)==(Number(a.match(tf)[4]||null)||null):!0;for(var f in th)(d=O(th[f]))&&(c||wh(a,f))&&(b[f]=d);if(c||wh(a,"X-YouTube-Utc-Offset"))b["X-YouTube-Utc-Offset"]=-(new Date).getTimezoneOffset();return b}
function wh(a,b){var c=O("CORS_HEADER_WHITELIST")||{},d=uf(a.match(tf)[3]||null);return d?(c=c[d])?Ia(c,b):!1:!0}
function xh(a,b){var c=b.format||"JSON";a=yh(a,b);var d=zh(a,b),e=!1,f,g=Ah(a,function(a){if(!e){e=!0;f&&window.clearTimeout(f);a:switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:var d=!0;break a;default:d=!1}var g=null;if(d||400<=a.status&&500>a.status)g=Bh(c,a,b.Pb);if(d)a:if(a&&204==a.status)d=!0;else{switch(c){case "XML":d=0==parseInt(g&&g.return_code,10);break a;case "RAW":d=!0;break a}d=!!g}g=g||{};var h=b.context||m;d?b.onSuccess&&
b.onSuccess.call(h,a,g):b.onError&&b.onError.call(h,a,g);b.ba&&b.ba.call(h,a,g)}},b.method,d,b.headers,b.responseType,b.withCredentials);
b.xb&&0<b.timeout&&(f=P(function(){e||(e=!0,g.abort(),window.clearTimeout(f),b.xb.call(b.context||m,g))},b.timeout))}
function yh(a,b){b.Rb&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=O("XSRF_FIELD_NAME",void 0),d=b.Ha;if(d){d[c]&&delete d[c];d=d||{};var e=a.split("#",2);c=e[0];e=1<e.length?"#"+e[1]:"";var f=c.split("?",2);c=f[0];f=Cg(f[1]||"");for(var g in d)f[g]=d[g];a=Af(c,f)+e}return a}
function zh(a,b){var c=O("XSRF_FIELD_NAME",void 0),d=O("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.L,g=O("XSRF_FIELD_NAME",void 0),h;b.headers&&(h=b.headers["Content-Type"]);b.Qb||uf(a.match(tf)[3]||null)&&!b.withCredentials&&uf(a.match(tf)[3]||null)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.L&&b.L[g]||(f||(f={}),f[c]=d);f&&r(e)&&(e=Cg(e),db(e,f),e=b.Ab&&"JSON"==b.Ab?JSON.stringify(e):yf(e));if(!(c=e)&&(c=f)){a:{for(var l in f){f=!1;break a}f=!0}c=!f}!uh&&
c&&"POST"!=b.method&&(uh=!0,Ef(Error("AJAX request with postData should use POST")));return e}
function Bh(a,b,c){var d=null;switch(a){case "JSON":a=b.responseText;b=b.getResponseHeader("Content-Type")||"";a&&0<=b.indexOf("json")&&(d=JSON.parse(a));break;case "XML":if(b=(b=b.responseXML)?Ch(b):null)d={},A(b.getElementsByTagName("*"),function(a){d[a.tagName]=Dh(a)})}c&&Eh(d);
return d}
function Eh(a){if(ta(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Qb(a[b]);a[c]=d}else Eh(a[b])}}
function Ch(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Dh(a){var b="";A(a.childNodes,function(a){b+=a.nodeValue});
return b}
function Ah(a,b,c,d,e,f,g){function h(){4==(l&&"readyState"in l?l.readyState:0)&&b&&Df(b)(l)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var l=sh();if(!l)return null;"onloadend"in l?l.addEventListener("loadend",h,!1):l.onreadystatechange=h;l.open(c,a,!0);f&&(l.responseType=f);g&&(l.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=vh(a,e))for(var n in e)l.setRequestHeader(n,e[n]),"content-type"==n.toLowerCase()&&(c=!1);c&&l.setRequestHeader("Content-Type","application/x-www-form-urlencoded");l.send(d);return l}
;function Fh(){var a=new mf;(a=a.isAvailable()?new sf(a,"yt.innertube"):null)||(a=new nf("yt.innertube"),a=a.isAvailable()?a:null);this.b=a?new hf(a):null;this.f=document.domain||window.location.hostname}
Fh.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.b)try{this.b.set(a,b,Aa()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(de(b))}catch(f){return}else e=escape(b);b=this.f;Hc.set(""+a,e,c,"/",void 0===b?"youtube.com":b,!1)};
Fh.prototype.get=function(a,b){var c=void 0,d=!this.b;if(!d)try{c=this.b.get(a)}catch(e){d=!0}if(d&&(c=Hc.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
Fh.prototype.remove=function(a){this.b&&this.b.remove(a);var b=this.f;Hc.remove(""+a,"/",void 0===b?"youtube.com":b)};new Fh;var Gh=Aa().toString();var Hh;a:{if(window.crypto&&window.crypto.getRandomValues)try{var Ih=Array(16),Jh=new Uint8Array(16);window.crypto.getRandomValues(Jh);for(var Kh=0;Kh<Ih.length;Kh++)Ih[Kh]=Jh[Kh];Hh=Ih;break a}catch(a){}for(var Lh=Array(16),Mh=0;16>Mh;Mh++){for(var Nh=Aa(),Oh=0;Oh<Nh%23;Oh++)Lh[Mh]=Math.random();Lh[Mh]=Math.floor(256*Math.random())}if(Gh)for(var Ph=1,Qh=0;Qh<Gh.length;Qh++)Lh[Ph%16]=Lh[Ph%16]^Lh[(Ph-1)%16]/4^Gh.charCodeAt(Qh),Ph++;Hh=Lh}
for(var Rh=Hh,Sh=[],Th=0;Th<Rh.length;Th++)Sh.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(Rh[Th]&63));function Uh(){xg.call(this,"button");this.b=null;this.g=[];this.f={}}
y(Uh,xg);oa(Uh);k=Uh.prototype;k.register=function(){Y(this,"click",this.Ia);Y(this,"keydown",this.ta);Y(this,"keypress",this.ua);yg(this,"page-scroll",this.kb)};
k.unregister=function(){Z(this,"click",this.Ia);Z(this,"keydown",this.ta);Z(this,"keypress",this.ua);Vh(this);this.f={};Uh.w.unregister.call(this)};
k.Ia=function(a){a&&!a.disabled&&(this.toggle(a),this.click(a))};
k.ta=function(a,b,c){if(!(c.altKey||c.ctrlKey||c.shiftKey||c.metaKey)&&(b=Wh(this,a))){var d=function(a){var b="";a.tagName&&(b=a.tagName.toLowerCase());return"ul"==b||"table"==b},e;
d(b)?e=b:e=jc(b,d);if(e){e=e.tagName.toLowerCase();if("ul"==e)var f=this.rb;else"table"==e&&(f=this.qb);f&&Xh(this,a,b,c,v(f,this))}}};
k.kb=function(){var a=this.f,b=0;for(d in a)b++;if(0!=b)for(var c in a){b=a[c];var d=G(b.activeButtonNode||b.parentNode,X(this));if(void 0==d||void 0==b)break;Yh(this,d,b,!0)}};
function Xh(a,b,c,d,e){var f=dh(c),g=9==d.keyCode;if(g||32==d.keyCode||13==d.keyCode)if(d=Zh(a,c)){if(p(d.firstElementChild))b=d.firstElementChild;else for(b=d.firstChild;b&&1!=b.nodeType;)b=b.nextSibling;if("a"==b.tagName.toLowerCase()){var h=void 0===h?{}:h;var l=void 0===l?"":l;var n=void 0===n?window:n;n=n.location;h=Af(b.href,h)+l;h instanceof Jb||h instanceof Jb||(h=h.Z?h.Y():String(h),Lb.test(h)||(h="about:invalid#zClosurez"),h=Mb(h));h instanceof Jb&&h.constructor===Jb&&h.f===Kb?h=h.b:(pa(h),
h="type_error:SafeUrl");n.href=h}else sg(b)}else g&&$h(a,b);else f?27==d.keyCode?(Zh(a,c),$h(a,b)):e(b,c,d):(h=K(b,X(a,"reverse"))?38:40,d.keyCode==h&&(sg(b),d.preventDefault()))}
k.ua=function(a,b,c){c.altKey||c.ctrlKey||c.shiftKey||c.metaKey||(a=Wh(this,a),dh(a)&&c.preventDefault())};
function Zh(a,b){var c=X(a,"menu-item-highlight"),d=F(c,b);d&&M(d,c);return d}
function ai(a,b,c){L(c,X(a,"menu-item-highlight"));var d=c.getAttribute("id");d||(d=X(a,"item-id-"+ua(c)),c.setAttribute("id",d));b.setAttribute("aria-activedescendant",d)}
k.qb=function(a,b,c){var d=Zh(this,b);if(d){var e=hg("table",b);b=Xb(document,"td",null,e);d=bi(d,b,Xb(document,"td",null,hg("tr",e)).length,c);-1!=d&&(ai(this,a,b[d]),c.preventDefault())}};
k.rb=function(a,b,c){if(40==c.keyCode||38==c.keyCode){var d=Zh(this,b);d&&(b=Ea(Xb(document,"li",null,b),dh),ai(this,a,b[bi(d,b,1,c)]),c.preventDefault())}};
function bi(a,b,c,d){var e=b.length;a=Da(b,a);if(-1==a)if(38==d.keyCode)a=e-c;else{if(37==d.keyCode||38==d.keyCode||40==d.keyCode)a=0}else 39==d.keyCode?(a%c==c-1&&(a-=c),a+=1):37==d.keyCode?(0==a%c&&(a+=c),--a):38==d.keyCode?(a<c&&(a+=e),a-=c):40==d.keyCode&&(a>=e-c&&(a-=e),a+=c);return a}
function ci(a,b){var c=b.iframeMask;c||(c=document.createElement("IFRAME"),c.src='javascript:""',c.className=X(a,"menu-mask"),fh(c),b.iframeMask=c);return c}
function Yh(a,b,c,d){var e=G(b,X(a,"group")),f=!!a.i(b,"button-menu-ignore-group");e=e&&!f?e:b;f=9;var g=8,h=ye(b);if(K(b,X(a,"reverse"))){f=8;g=9;h=h.top+"px";try{c.style.maxHeight=h}catch(t){}}K(b,"flip")&&(K(b,X(a,"reverse"))?(f=12,g=13):(f=13,g=12));var l;a.i(b,"button-has-sibling-menu")?l=re(e):a.i(b,"button-menu-root-container")&&(l=di(a,b));C&&!Eb("8")&&(l=null);if(l){var n=ye(l);n=new je(-n.top,n.left,n.top,-n.left)}l=new D(0,1);K(b,X(a,"center-menu"))&&(l.x-=Math.round((we(c).width-we(b).width)/
2));d&&(l.y+=bc(document).y);if(a=ci(a,b))b=we(c),a.style.width=b.width+"px",a.style.height=b.height+"px",He(e,f,a,g,l,n,197),d&&le(a,"position","fixed");He(e,f,c,g,l,n,197)}
function di(a,b){if(a.i(b,"button-menu-root-container")){var c=a.i(b,"button-menu-root-container");return G(b,c)}return document.body}
k.Ka=function(a){if(a){var b=Wh(this,a);if(b){a.setAttribute("aria-pressed","true");a.setAttribute("aria-expanded","true");b.originalParentNode=b.parentNode;b.activeButtonNode=a;b.parentNode.removeChild(b);var c;this.i(a,"button-has-sibling-menu")?c=a.parentNode:c=di(this,a);c.appendChild(b);b.style.minWidth=a.offsetWidth-2+"px";var d=ci(this,a);d&&c.appendChild(d);(c=!!this.i(a,"button-menu-fixed"))&&(this.f[eg(a).toString()]=b);Yh(this,a,b,c);Mf("yt-uix-button-menu-before-show",a,b);eh(b);d&&eh(d);
this.N(a,"button-menu-action",!0);L(a,X(this,"active"));b=v(this.Ja,this,a,!1);d=v(this.Ja,this,a,!0);c=v(this.Cb,this,a,void 0);this.b&&Wh(this,this.b)==Wh(this,a)||Vh(this);Q("yt-uix-button-menu-show",a);W(this.g);this.g=[V(document,"click",d),V(document,"contextmenu",b),V(window,"resize",c)];this.b=a}}};
function $h(a,b){if(b){var c=Wh(a,b);if(c){a.b=null;b.setAttribute("aria-pressed","false");b.setAttribute("aria-expanded","false");b.removeAttribute("aria-activedescendant");fh(c);a.N(b,"button-menu-action",!1);var d=ci(a,b),e=eg(c).toString();delete a.f[e];P(function(){d&&d.parentNode&&(fh(d),d.parentNode.removeChild(d));c.originalParentNode&&(c.parentNode.removeChild(c),c.originalParentNode.appendChild(c),c.originalParentNode=null,c.activeButtonNode=null)},1)}e=G(b,X(a,"group"));
var f=[X(a,"active")];e&&f.push(X(a,"group-active"));Pd(b,f);Q("yt-uix-button-menu-hide",b);W(a.g);a.g.length=0}}
k.Cb=function(a,b){var c=Wh(this,a);if(c){b&&(b instanceof Nb?c.innerHTML=Pb(b):ic(c,b));var d=!!this.i(a,"button-menu-fixed");Yh(this,a,c,d)}};
k.Ja=function(a,b,c){c=qg(c);var d=G(c,X(this));if(d){d=Wh(this,d);var e=Wh(this,a);if(d==e)return}d=G(c,X(this,"menu"));e=d==Wh(this,a);var f=K(c,X(this,"menu-item")),g=K(c,X(this,"menu-close"));if(!d||e&&(f||g))$h(this,a),d&&b&&this.i(a,"button-menu-indicate-selected")&&((a=F(X(this,"content"),a))&&ic(a,qc(c)),ei(this,d,c))};
function ei(a,b,c){var d=X(a,"menu-item-selected");A(Wb(d,b),function(a){M(a,d)});
L(c.parentNode,d)}
function Wh(a,b){if(!b.widgetMenu){var c=a.i(b,"button-menu-id");c=c&&E(c);var d=X(a,"menu");c?Od(c,[d,X(a,"menu-external")]):c=F(d,b);b.widgetMenu=c}return b.widgetMenu}
k.isToggled=function(a){return K(a,X(this,"toggled"))};
k.toggle=function(a){if(this.i(a,"button-toggle")){var b=G(a,X(this,"group")),c=X(this,"toggled"),d=K(a,c);if(b&&this.i(b,"button-toggle-group")){var e=this.i(b,"button-toggle-group");A(Wb(X(this),b),function(b){b!=a||"optional"==e&&d?(M(b,c),b.removeAttribute("aria-pressed")):(L(a,c),b.setAttribute("aria-pressed","true"))})}else d?a.removeAttribute("aria-pressed"):a.setAttribute("aria-pressed","true"),Sd(a,c)}};
k.click=function(a){if(Wh(this,a)){var b=Wh(this,a);if(b){var c=G(b.activeButtonNode||b.parentNode,X(this));c&&c!=a?($h(this,c),P(v(this.Ka,this,a),1)):dh(b)?$h(this,a):this.Ka(a)}a.focus()}this.N(a,"button-action")};
function Vh(a){a.b&&$h(a,a.b)}
;function fi(a){xg.call(this,a);this.g=null}
y(fi,xg);k=fi.prototype;k.B=function(a){var b=xg.prototype.B.call(this,a);return b?b:a};
k.register=function(){yg(this,"yt-uix-kbd-nav-move-out-done",this.hide)};
k.dispose=function(){gi(this);fi.w.dispose.call(this)};
k.i=function(a,b){var c=fi.w.i.call(this,a,b);return c?c:(c=fi.w.i.call(this,a,"card-config"))&&(c=u(c))&&c[b]?c[b]:null};
k.show=function(a){var b=this.B(a);if(b){L(b,X(this,"active"));var c=hi(this,a,b);if(c){c.cardTargetNode=a;c.cardRootNode=b;ii(this,a,c);var d=X(this,"card-visible"),e=this.i(a,"card-delegate-show")&&this.i(b,"card-action");this.N(b,"card-action",a);this.g=a;fh(c);P(v(function(){e||(eh(c),Q("yt-uix-card-show",b,a,c));ji(c);L(c,d);Q("yt-uix-kbd-nav-move-in-to",c)},this),10)}}};
function hi(a,b,c){var d=c||b,e=X(a,"card");c=ki(a,d);var f=E(X(a,"card")+eg(d));if(f)return a=F(X(a,"card-body"),f),hc(a,c)||(ec(c),a.appendChild(c)),f;f=document.createElement("div");f.id=X(a,"card")+eg(d);f.className=e;(d=a.i(d,"card-class"))&&Od(f,d.split(/\s+/));d=document.createElement("div");d.className=X(a,"card-border");b=a.i(b,"orientation")||"horizontal";e=document.createElement("div");e.className="yt-uix-card-border-arrow yt-uix-card-border-arrow-"+b;var g=document.createElement("div");
g.className=X(a,"card-body");a=document.createElement("div");a.className="yt-uix-card-body-arrow yt-uix-card-body-arrow-"+b;ec(c);g.appendChild(c);d.appendChild(a);d.appendChild(g);f.appendChild(e);f.appendChild(d);document.body.appendChild(f);return f}
function ii(a,b,c){var d=a.i(b,"orientation")||"horizontal",e=F(X(a,"anchor"),b)||b,f=a.i(b,"position"),g=!!a.i(b,"force-position"),h=a.i(b,"position-fixed");d="horizontal"==d;var l="bottomright"==f||"bottomleft"==f,n="topright"==f||"bottomright"==f;if(n&&l){var t=13;var z=8}else n&&!l?(t=12,z=9):!n&&l?(t=9,z=12):(t=8,z=13);var q=ze(document.body);f=ze(b);q!=f&&(t^=4);if(d){f=b.offsetHeight/2-12;var I=new D(-12,b.offsetHeight+6)}else f=b.offsetWidth/2-6,I=new D(b.offsetWidth+6,-12);var w=we(c);f=
Math.min(f,(d?w.height:w.width)-24-6);6>f&&(f=6,d?I.y+=12-b.offsetHeight/2:I.x+=12-b.offsetWidth/2);w=null;g||(w=10);b=X(a,"card-flip");a=X(a,"card-reverse");Qd(c,b,n);Qd(c,a,l);w=He(e,t,c,z,I,null,w);!g&&w&&(w&48&&(n=!n,t^=4,z^=4),w&192&&(l=!l,t^=1,z^=1),Qd(c,b,n),Qd(c,a,l),He(e,t,c,z,I));h&&(e=parseInt(c.style.top,10),g=bc(document).y,le(c,"position","fixed"),le(c,"top",e-g+"px"));q&&(c.style.right="",e=ye(c),e.left=e.left||parseInt(c.style.left,10),g=$b(window),c.style.left="",c.style.right=g.width-
e.left-e.width+"px");e=F("yt-uix-card-body-arrow",c);g=F("yt-uix-card-border-arrow",c);d=d?l?"top":"bottom":!q&&n||q&&!n?"left":"right";e.setAttribute("style","");g.setAttribute("style","");e.style[d]=f+"px";g.style[d]=f+"px";l=F("yt-uix-card-arrow",c);n=F("yt-uix-card-arrow-background",c);l&&n&&(c="right"==d?we(c).width-f-13:f+11,f=c/Math.sqrt(2),l.style.left=c+"px",l.style.marginLeft="1px",n.style.marginLeft=-f+"px",n.style.marginTop=f+"px")}
k.hide=function(a){if(a=this.B(a)){var b=E(X(this,"card")+eg(a));b&&(M(a,X(this,"active")),M(b,X(this,"card-visible")),fh(b),this.g=null,b.cardTargetNode=null,b.cardRootNode=null,b.cardMask&&(ec(b.cardMask),b.cardMask=null))}};
function gi(a){a.g&&a.hide(a.g)}
k.Bb=function(a,b){var c=this.B(a);if(c){if(b){var d=ki(this,c);if(!d)return;b instanceof Nb?d.innerHTML=Pb(b):ic(d,b)}K(c,X(this,"active"))&&(c=hi(this,a,c),ii(this,a,c),eh(c),ji(c))}};
k.isActive=function(a){return(a=this.B(a))?K(a,X(this,"active")):!1};
function ki(a,b){var c=b.cardContentNode;if(!c){var d=X(a,"content"),e=X(a,"card-content");(c=(c=a.i(b,"card-id"))?E(c):F(d,b))||(c=document.createElement("div"));var f=c;M(f,d);L(f,e);b.cardContentNode=c}return c}
function ji(a){var b=a.cardMask;b||(b=document.createElement("IFRAME"),b.src='javascript:""',Od(b,["yt-uix-card-iframe-mask"]),a.cardMask=b);b.style.position=a.style.position;b.style.top=a.style.top;b.style.left=a.offsetLeft+"px";b.style.height=a.clientHeight+"px";b.style.width=a.clientWidth+"px";document.body.appendChild(b)}
;function li(){xg.call(this,"kbd-nav")}
var mi;y(li,xg);oa(li);k=li.prototype;k.register=function(){Y(this,"keydown",this.ra);yg(this,"yt-uix-kbd-nav-move-in",this.za);yg(this,"yt-uix-kbd-nav-move-in-to",this.sb);yg(this,"yt-uix-kbd-move-next",this.Aa);yg(this,"yt-uix-kbd-nav-move-to",this.R)};
k.unregister=function(){Z(this,"keydown",this.ra);W(mi)};
k.ra=function(a,b,c){var d=c.keyCode;if(a=G(a,X(this)))switch(d){case 13:case 32:this.za(a);break;case 27:c.preventDefault();c.stopImmediatePropagation();a:{for(c=Ud(a,"kbdNavMoveOut");!c;){c=G(a.parentElement,X(this));if(!c)break a;c=Ud(c,"kbdNavMoveOut")}c=E(c);this.R(c);Q("yt-uix-kbd-nav-move-out-done",c)}break;case 40:case 38:if((b=c.target)&&K(a,X(this,"list")))switch(d){case 40:this.Aa(b,a);break;case 38:d=document.activeElement==a,a=ni(a),b=a.indexOf(b),0>b&&!d||(b=d?a.length-1:(a.length+b-
1)%a.length,a[b].focus(),oi(this,a[b]))}c.preventDefault()}};
k.za=function(a){var b=Ud(a,"kbdNavMoveIn");b=E(b);pi(this,a,b);this.R(b)};
k.sb=function(a){var b=document;try{var c=b&&b.activeElement;var d=c&&c.nodeName?c:null}catch(e){d=null}pi(this,d,a);this.R(a)};
k.R=function(a){if(a)if(nc(a))a.focus();else{var b=jc(a,function(a){return gc(a)?nc(a):!1});
b?b.focus():(a.setAttribute("tabindex","-1"),a.focus())}};
function pi(a,b,c){if(b&&c)if(L(c,X(a)),a=b.id,a||(a="kbd-nav-"+Math.floor(1E6*Math.random()+1),b.id=a),b=a,Td&&c.dataset)c.dataset.kbdNavMoveOut=b;else{if(/-[a-z]/.test("kbdNavMoveOut"))throw Error("");c.setAttribute("data-"+"kbdNavMoveOut".replace(/([A-Z])/g,"-$1").toLowerCase(),b)}}
k.Aa=function(a,b){var c=document.activeElement==b,d=ni(b),e=d.indexOf(a);0>e&&!c||(c=c?0:(e+1)%d.length,d[c].focus(),oi(this,d[c]))};
function oi(a,b){if(b){var c=sc(b,"LI");c&&(L(c,X(a,"highlight")),mi=V(b,"blur",v(function(a){M(a,X(this,"highlight"));W(mi)},a,c)))}}
function ni(a){if("UL"!=a.tagName.toUpperCase())return[];a=Ea(fc(a),function(a){return"LI"==a.tagName.toUpperCase()});
return Ea(Fa(a,function(a){return dh(a)?jc(a,function(a){return gc(a)?nc(a):!1}):!1}),function(a){return!!a})}
;function qi(){xg.call(this,"menu");this.f=this.b=null;this.g={};this.o={};this.j=null}
y(qi,xg);oa(qi);function ri(a){var b=qi.v();if(K(a,X(b)))return a;var c=b.B(a);return c?c:G(a,X(b,"content"))==b.b?b.f:null}
k=qi.prototype;k.register=function(){Y(this,"click",this.qa);Y(this,"mouseenter",this.ib);yg(this,"page-scroll",this.lb);yg(this,"yt-uix-kbd-nav-move-out-done",function(a){a=this.B(a);si(this,a)});
this.j=new N};
k.unregister=function(){Z(this,"click",this.qa);this.f=this.b=null;W(Oa($a(this.g)));this.g={};Za(this.o,function(a){ec(a)},this);
this.o={};Md(this.j);this.j=null;qi.w.unregister.call(this)};
k.qa=function(a,b,c){a&&(b=ti(this,a),!b.disabled&&gg(c.target,b)&&ui(this,a))};
k.ib=function(a,b,c){a&&K(a,X(this,"hover"))&&gg(c.target,ti(this,a))&&ui(this,a,!0)};
k.lb=function(){this.b&&this.f&&vi(this,this.f,this.b)};
function vi(a,b,c){var d=wi(a,b);if(d){var e=we(c);if(e instanceof Sb){var f=e.height;e=e.width}else throw Error("missing height argument");d.style.width=ve(e,!0);d.style.height=ve(f,!0)}c==a.b&&(e=9,f=8,K(b,X(a,"reversed"))&&(e^=1,f^=1),K(b,X(a,"flipped"))&&(e^=4,f^=4),a=new D(0,1),d&&He(b,e,d,f,a,null,197),He(b,e,c,f,a,null,197))}
function ui(a,b,c){xi(a,b)&&!c?si(a,b):(yi(a,b),!a.b||gg(b,a.b)?a.La(b):$e(a.j,v(a.La,a,b)))}
k.La=function(a){if(a){var b=zi(this,a);if(b){Mf("yt-uix-menu-before-show",a,b);this.b?gg(a,this.b)||si(this,this.f):(this.f=a,this.b=b,K(a,X(this,"sibling-content"))||(ec(b),document.body.appendChild(b)),b.style.minWidth=ti(this,a).offsetWidth-2+"px");var c=wi(this,a);c&&b.parentNode&&b.parentNode.insertBefore(c,b.nextSibling);M(b,X(this,"content-hidden"));vi(this,a,b);Od(ti(this,a),[X(this,"trigger-selected"),"yt-uix-button-toggled"]);Q("yt-uix-menu-show",a);Ai(b);Bi(this,a);Q("yt-uix-kbd-nav-move-in-to",
b);var d=v(this.Db,this,a),e=v(this.ob,this,a);c=ua(a).toString();this.g[c]=[V(b,"click",e),V(document,"click",d)];K(a,X(this,"indicate-selected"))&&(d=v(this.pb,this,a),this.g[c].push(V(b,"click",d)));K(a,X(this,"hover"))&&(a=v(this.jb,this,a),this.g[c].push(V(document,"mousemove",a)))}}};
k.jb=function(a,b){var c=qg(b);c&&(gg(c,ti(this,a))||Ci(this,c)||Di(this,a))};
k.Db=function(a,b){var c=qg(b);if(c){if(Ci(this,c)){var d=G(c,X(this,"content")),e=sc(c,"LI");e&&d&&hc(d,e)&&Mf("yt-uix-menu-item-clicked",c);c=G(c,X(this,"close-on-select"));if(!c)return;d=ri(c)}si(this,d||a)}};
function yi(a,b){if(b){var c=G(b,X(a,"content"));c&&A(Wb(X(a),c),function(a){!gg(a,b)&&xi(this,a)&&Di(this,a)},a)}}
function si(a,b){if(b){var c=[];c.push(b);var d=zi(a,b);d&&(d=Wb(X(a),d),d=Ka(d),c=c.concat(d),A(c,function(a){xi(this,a)&&Di(this,a)},a))}}
function Di(a,b){if(b){var c=zi(a,b);Pd(ti(a,b),[X(a,"trigger-selected"),"yt-uix-button-toggled"]);L(c,X(a,"content-hidden"));var d=zi(a,b);d&&Yb(d,{"aria-expanded":"false"});(d=wi(a,b))&&d.parentNode&&ec(d);c&&c==a.b&&(a.f.appendChild(c),a.b=null,a.f=null,a.j&&a.j.F("ROOT_MENU_REMOVED"));Q("yt-uix-menu-hide",b);c=ua(b).toString();W(a.g[c]);delete a.g[c]}}
k.ob=function(a,b){var c=qg(b);c&&Ei(this,a,c)};
k.pb=function(a,b){var c=qg(b);if(c){var d=ti(this,a);if(d&&(c=sc(c,"LI")))if(c=qc(c).trim(),d.hasChildNodes()){var e=Uh.v();(d=F(X(e,"content"),d))&&ic(d,c)}else ic(d,c)}};
function Bi(a,b){var c=zi(a,b);if(c){A(c.children,function(a){"LI"==a.tagName&&Yb(a,{role:"menuitem"})});
Yb(c,{"aria-expanded":"true"});var d=c.id;d||(d="aria-menu-id-"+ua(c),c.id=d);(c=ti(a,b))&&Yb(c,{"aria-controls":d})}}
function Ei(a,b,c){var d=zi(a,b);d&&K(b,X(a,"checked"))&&(a=sc(c,"LI"))&&(a=F("yt-ui-menu-item-checked-hid",a))&&(A(Wb("yt-ui-menu-item-checked",d),function(a){Rd(a,"yt-ui-menu-item-checked","yt-ui-menu-item-checked-hid")}),Rd(a,"yt-ui-menu-item-checked-hid","yt-ui-menu-item-checked"))}
function xi(a,b){var c=zi(a,b);return c?!K(c,X(a,"content-hidden")):!1}
function Ai(a){A(Xb(document,"UL",null,a),function(a){a.tabIndex=0;var b=li.v();Od(a,[X(b),X(b,"list")])})}
function zi(a,b){var c=Pf(b,"menu-content-id");return c&&(c=E(c))?(Od(c,[X(a,"content"),X(a,"content-external")]),c):b==a.f?a.b:F(X(a,"content"),b)}
function wi(a,b){var c=ua(b).toString(),d=a.o[c];if(!d){d=document.createElement("IFRAME");d.src='javascript:""';var e=[X(a,"mask")];A(Nd(b),function(a){e.push(a+"-mask")});
Od(d,e);a.o[c]=d}return d||null}
function ti(a,b){return F(X(a,"trigger"),b)}
function Ci(a,b){return gg(b,a.b)||gg(b,a.f)}
;function Fi(){fi.call(this,"clickcard");this.b={};this.f={}}
y(Fi,fi);oa(Fi);k=Fi.prototype;k.register=function(){Fi.w.register.call(this);Y(this,"click",this.na,"target");Y(this,"click",this.ma,"close")};
k.unregister=function(){Fi.w.unregister.call(this);Z(this,"click",this.na,"target");Z(this,"click",this.ma,"close");for(var a in this.b)W(this.b[a]);this.b={};for(a in this.f)W(this.f[a]);this.f={}};
k.na=function(a,b,c){c.preventDefault();b=sc(c.target,"button");if(!b||!b.disabled){if(b=this.i(a,"card-target"))a=document,a=r(b)?a.getElementById(b):b;b=this.B(a);this.i(b,"disabled")||(K(b,X(this,"active"))?(this.hide(a),M(b,X(this,"active"))):(this.show(a),L(b,X(this,"active"))))}};
k.show=function(a){Fi.w.show.call(this,a);var b=this.B(a),c=ua(a).toString();if(!Pf(b,"click-outside-persists")){if(this.b[c])return;b=V(document,"click",v(this.oa,this,a));var d=V(window,"blur",v(this.oa,this,a));this.b[c]=[b,d]}a=V(window,"resize",v(this.Bb,this,a,void 0));this.f[c]=a};
k.hide=function(a){Fi.w.hide.call(this,a);a=ua(a).toString();var b=this.b[a];b&&(W(b),this.b[a]=null);if(b=this.f[a])W(b),delete this.f[a]};
k.oa=function(a,b){var c="yt-uix"+(this.l?"-"+this.l:"")+"-card",d=null;b.target&&(d=G(b.target,c)||G(ri(b.target),c));(d=d||G(document.activeElement,c)||G(ri(document.activeElement),c))||this.hide(a)};
k.ma=function(a){(a=G(a,X(this,"card")))&&(a=a.cardTargetNode)&&this.hide(a)};function Gi(){fi.call(this,"hovercard")}
y(Gi,fi);oa(Gi);k=Gi.prototype;k.register=function(){Y(this,"mouseenter",this.va,"target");Y(this,"mouseleave",this.xa,"target");Y(this,"mouseenter",this.wa,"card");Y(this,"mouseleave",this.ya,"card")};
k.unregister=function(){Z(this,"mouseenter",this.va,"target");Z(this,"mouseleave",this.xa,"target");Z(this,"mouseenter",this.wa,"card");Z(this,"mouseleave",this.ya,"card")};
k.va=function(a){if(Hi!=a){Hi&&(this.hide(Hi),Hi=null);var b=v(this.show,this,a),c=parseInt(this.i(a,"delay-show"),10);b=P(b,-1<c?c:200);Nf(a,"card-timer",b.toString());Hi=a;a.alt&&(Nf(a,"card-alt",a.alt),a.alt="");a.title&&(Nf(a,"card-title",a.title),a.title="")}};
k.xa=function(a){var b=parseInt(this.i(a,"card-timer"),10);window.clearTimeout(b);this.B(a).isCardHidable=!0;b=parseInt(this.i(a,"delay-hide"),10);b=-1<b?b:200;P(v(this.mb,this,a),b);if(b=this.i(a,"card-alt"))a.alt=b;if(b=this.i(a,"card-title"))a.title=b};
k.mb=function(a){this.B(a).isCardHidable&&(this.hide(a),Hi=null)};
k.wa=function(a){a&&(a.cardRootNode.isCardHidable=!1)};
k.ya=function(a){a&&this.hide(a.cardTargetNode)};
var Hi=null;function Ii(a,b,c,d,e,f){this.b=a;this.A=null;this.g=F("yt-dialog-fg",this.b)||this.b;if(a=F("yt-dialog-title",this.g)){var g="yt-dialog-title-"+ua(this.g);a.setAttribute("id",g);this.g.setAttribute("aria-labelledby",g)}this.g.setAttribute("tabindex","-1");this.P=F("yt-dialog-focus-trap",this.b);this.ea=!1;this.j=new N;this.C=[];this.C.push(rg(this.b,v(this.tb,this),"yt-dialog-dismiss"));this.C.push(V(this.P,"focus",v(this.hb,this),!0));Ji(this);this.Pa=b;this.Wa=c;this.Va=d;this.J=e;this.Xa=f;this.o=
this.l=null}
var Ki={LOADING:"loading",Gb:"content",Nb:"working"};function Li(a,b){a.S()||a.j.subscribe("post-all",b)}
function Ji(a){a=F("yt-dialog-fg-content",a.b);var b=[];Za(Ki,function(a){b.push("yt-dialog-show-"+a)});
Pd(a,b);L(a,"yt-dialog-show-content")}
k=Ii.prototype;
k.show=function(){if(!this.S()){this.A=document.activeElement;if(!this.Va){this.f||(this.f=E("yt-dialog-bg"),this.f||(this.f=document.createElement("div"),this.f.id="yt-dialog-bg",this.f.className="yt-dialog-bg",document.body.appendChild(this.f)));var a=window,b=a.document;var c=0;if(b){c=b.body;var d=b.documentElement;if(d&&c)if(a=$b(a).height,ac(b)&&d.scrollHeight)c=d.scrollHeight!=a?d.scrollHeight:d.offsetHeight;else{b=d.scrollHeight;var e=d.offsetHeight;d.clientHeight!=e&&(b=c.scrollHeight,e=
c.offsetHeight);c=b>a?b>e?b:e:b<e?b:e}else c=0}this.f.style.height=c+"px";eh(this.f)}this.sa();c=Mi(this);Ni(c);this.l=V(document,"keydown",v(this.nb,this));c=this.b;d=Jf("player-added",this.sa,this);Nf(c,"player-ready-pubsub-key",d);this.Wa&&(this.o=V(document,"click",v(this.zb,this)));eh(this.b);this.g.setAttribute("tabindex","0");Oi(this);this.J||L(document.body,"yt-dialog-active");Vh(Uh.v());gi(Fi.v());gi(Gi.v());Q("yt-ui-dialog-show-complete",this)}};
function Pi(){return Ga(Wb("yt-dialog"),function(a){return dh(a)})}
k.sa=function(){if(!this.Xa){var a=this.b;Qd(document.body,"hide-players",!0);a&&Qd(a,"preserve-players",!0)}};
function Mi(a){var b=Xb(document,"iframe",null,a.b);A(b,function(a){var b=Pf(a,"onload");b&&(b=u(b))&&V(a,"load",b);if(b=Pf(a,"src"))a.src=b},a);
return Ka(b)}
function Ni(a){A(document.getElementsByTagName("iframe"),function(b){-1==Da(a,b)&&L(b,"iframe-hid")})}
function Qi(){A(Wb("iframe-hid"),function(a){M(a,"iframe-hid")})}
k.tb=function(a){a=a.currentTarget;a.disabled||(a=Pf(a,"action")||"",this.dismiss(a))};
k.dismiss=function(a){if(!this.S()){this.j.F("pre-all");this.j.F("pre-"+a);fh(this.b);gi(Fi.v());gi(Gi.v());this.g.setAttribute("tabindex","-1");Pi()||(fh(this.f),this.J||M(document.body,"yt-dialog-active"),jg(),Qi());this.l&&(W(this.l),this.l=null);this.o&&(W(this.o),this.o=null);var b=this.b;if(b){var c=Pf(b,"player-ready-pubsub-key");c&&(Lf(c),Qf(b,"player-ready-pubsub-key"))}this.j.F("post-all");Q("yt-ui-dialog-hide-complete",this);"cancel"==a&&Q("yt-ui-dialog-cancelled",this);this.j&&this.j.F("post-"+
a);this.A&&this.A.focus()}};
k.setTitle=function(a){ic(F("yt-dialog-title",this.b),a)};
k.nb=function(a){P(v(function(){this.Pa||27!=a.keyCode||this.dismiss("cancel")},this),0);
9==a.keyCode&&a.shiftKey&&K(document.activeElement,"yt-dialog-fg")&&a.preventDefault()};
k.zb=function(a){"yt-dialog-base"==a.target.className&&this.dismiss("cancel")};
k.S=function(){return this.ea};
k.dispose=function(){dh(this.b)&&this.dismiss("dispose");W(this.C);this.C.length=0;P(v(function(){this.A=null},this),0);
this.P=this.g=null;this.j.dispose();this.j=null;this.ea=!0};
k.hb=function(a){a.stopPropagation();Oi(this)};
function Oi(a){P(v(function(){this.g&&this.g.focus()},a),0)}
x("yt.ui.Dialog",Ii);function Ri(){xg.call(this,"overlay");this.j=this.f=this.g=this.b=null}
y(Ri,xg);oa(Ri);k=Ri.prototype;k.register=function(){Y(this,"click",this.ca,"target");Y(this,"click",this.hide,"close");Si(this)};
k.unregister=function(){Ri.w.unregister.call(this);Z(this,"click",this.ca,"target");Z(this,"click",this.hide,"close");this.j&&(Lf(this.j),this.j=null);this.f&&(W(this.f),this.f=null)};
k.ca=function(a){if(!this.b||!dh(this.b.b)){var b=this.B(a);a=Ti(b,a);b||(b=a?a.overlayParentNode:null);if(b&&a){var c=!!this.i(b,"disable-shortcuts")||!1,d=!!this.i(b,"disable-outside-click-dismiss")||!1;this.b=new Ii(a,c);this.g=b;var e=F("yt-dialog-fg",a);if(e){var f=this.i(b,"overlay-class")||"",g=this.i(b,"overlay-style")||"default",h=this.i(b,"overlay-shape")||"default";f=f?f.split(" "):[];f.push(X(this,g));f.push(X(this,h));Od(e,f)}this.b.show();Q("yt-uix-kbd-nav-move-to",e||a);Si(this);c||
d||(c=v(function(a){K(a.target,"yt-dialog-base")&&Ui(this)},this),this.f=V(F("yt-dialog-base",a),"click",c));
this.N(b,"overlay-shown");Q("yt-uix-overlay-shown",b)}}};
function Si(a){a.j||(a.j=Jf("yt-uix-overlay-hide",Vi));a.b&&Li(a.b,function(){var a=Ri.v();a.g=null;a.b.dispose();a.b=null})}
function Ui(a){if(a.b){var b=a.g;a.b.dismiss("overlayhide");b&&a.N(b,"overlay-hidden");a.g=null;a.f&&(W(a.f),a.f=null);a.b=null}}
function Ti(a,b){var c;if(a)if(c=F("yt-dialog",a)){var d=E("body-container");d&&(d.appendChild(c),a.overlayContentNode=c,c.overlayParentNode=a)}else c=a.overlayContentNode;else b&&(c=G(b,"yt-dialog"));return c}
function Wi(){var a=Ri.v();if(a.g)a=F("yt-dialog-fg-content",a.g.overlayContentNode);else a:{if(a=Wb("yt-dialog-fg-content"))for(var b=0;b<a.length;b++){var c=G(a[b],"yt-dialog");if(dh(c)){a=a[b];break a}}a=null}return a}
k.hide=function(a){a&&a.disabled||Q("yt-uix-overlay-hide")};
function Vi(){Ui(Ri.v())}
k.show=function(a){this.ca(a)};var Xi={},Yi=[];function Zi(a){a=G(a,"yt-uix-button-subscription-container");return F("yt-dialog",F("unsubscribe-confirmation-overlay-container",a))}
function $i(a,b){W(Yi);Yi.length=0;Xi[b]||(Xi[b]=Zi(a));Ri.v().show(Xi[b]);var c=Wi();return new Ke(function(a){Yi.push(rg(c,function(){a()},"overlay-confirmation-unsubscribe-button"))})}
;function aj(){var a=O("PLAYER_CONFIG");return a&&a.args&&void 0!==a.args.authuser?!0:!(!O("SESSION_INDEX")&&!O("LOGGED_IN"))}
;function bj(){xg.call(this,"subscription-button")}
y(bj,xg);oa(bj);bj.prototype.register=function(){Y(this,"click",this.da);zg(this,Og,this.Ca);zg(this,Pg,this.Ba);zg(this,Qg,this.wb);zg(this,Tg,this.Ca);zg(this,Ug,this.Ba);zg(this,Vg,this.yb);zg(this,Xg,this.vb);zg(this,Yg,this.ub)};
bj.prototype.unregister=function(){Z(this,"click",this.da);bj.w.unregister.call(this)};
bj.prototype.isSubscribed=function(a){return!!this.i(a,"is-subscribed")};
var cj={fa:"hover-enabled",Na:"yt-uix-button-subscribe",Oa:"yt-uix-button-subscribed",Eb:"ypc-enabled",Qa:"yt-uix-button-subscription-container",Ra:"yt-subscription-button-disabled-mask-container"},dj={Fb:"channel-external-id",Sa:"subscriber-count-show-when-subscribed",Ta:"subscriber-count-tooltip",Ua:"subscriber-count-title",Hb:"href",Ib:"insecure",ga:"is-subscribed",Jb:"parent-url",Kb:"clicktracking",Ya:"show-unsub-confirm-dialog",Lb:"show-unsub-confirm-time-frame",Za:"style-type",ha:"subscribed-timestamp",
ia:"subscription-id",Mb:"target",ab:"ypc-enabled"};k=bj.prototype;k.da=function(a){var b=this.i(a,"href"),c=this.i(a,"insecure");if(b)a=this.i(a,"target")||"_self",window.open(b,a);else if(!c)if(aj()){b=this.i(a,"channel-external-id");c=this.i(a,"clicktracking");var d=ej(this,a),e=this.i(a,"parent-url");if(this.i(a,"is-subscribed")){var f=this.i(a,"subscription-id"),g=new Kg(b,f,d,a,c,e);fj(this,a)?$i(a,b).then(function(){U(Sg,g)}):U(Sg,g)}else U(Ng,new Ig(b,d,c,e))}else gj(this,a)};
k.Ca=function(a){this.M(a.b,this.Ea,!0)};
k.Ba=function(a){this.M(a.b,this.Ea,!1)};
k.wb=function(a){this.M(a.b,this.Fa,!0,a.f)};
k.yb=function(a){this.M(a.b,this.Fa,!1)};
k.vb=function(a){this.M(a.b,this.gb)};
k.ub=function(a){this.M(a.b,this.fb)};
k.Fa=function(a,b,c){b?(Nf(a,dj.ga,"true"),c&&Nf(a,dj.ia,c),this.i(a,dj.Ya)&&(b=new Kd,Nf(a,dj.ha,(b.getTime()/1E3).toString()))):(Qf(a,dj.ga),Qf(a,dj.ha),Qf(a,dj.ia));hj(this,a)};
function ej(a,b){if(!a.i(b,"ypc-enabled"))return null;var c=a.i(b,"ypc-item-type"),d=a.i(b,"ypc-item-id");return{itemType:c,itemId:d,subscriptionElement:b}}
k.Ea=function(a,b){var c=G(a,cj.Qa);Qd(c,cj.Ra,b);a.setAttribute("aria-busy",b?"true":"false");a.disabled=b};
function hj(a,b){var c=a.i(b,dj.Za),d=!!a.i(b,"is-subscribed");c="-"+c;var e=cj.Oa+c;Qd(b,cj.Na+c,!d);Qd(b,e,d);a.i(b,dj.Ta)&&!a.i(b,dj.Sa)&&(c=X(gh.v()),Qd(b,c,!d),b.title=d?"":a.i(b,dj.Ua));d?P(function(){L(b,cj.fa)},1E3):M(b,cj.fa)}
k.gb=function(a){var b=!!this.i(a,"ypc-item-type"),c=!!this.i(a,"ypc-item-id");!this.i(a,"ypc-enabled")&&b&&c&&(L(a,"ypc-enabled"),Nf(a,dj.ab,"true"))};
k.fb=function(a){this.i(a,"ypc-enabled")&&(M(a,"ypc-enabled"),Qf(a,"ypc-enabled"))};
function ij(a,b){return Ea(Wb(X(a)),function(a){return b==this.i(a,"channel-external-id")},a)}
k.cb=function(a,b,c){var d=Na(arguments,2);A(a,function(a){b.apply(this,Ja(a,d))},this)};
k.M=function(a,b,c){var d=ij(this,a);this.cb.apply(this,Ja([d],Na(arguments,1)))};
function gj(a,b){var c=v(function(a){a.discoverable_subscriptions&&Cf("SUBSCRIBE_EMBED_DISCOVERABLE_SUBSCRIPTIONS",a.discoverable_subscriptions);this.da(b)},a);
oh(c)}
function fj(a,b){if(!a.i(b,"show-unsub-confirm-dialog"))return!1;var c=a.i(b,"show-unsub-confirm-time-frame");return"always"==c||"ten_minutes"==c&&(c=parseInt(a.i(b,"subscribed-timestamp"),10),(new Kd).getTime()<1E3*(c+600))?!0:!1}
;function jj(a){this.b=a;this.D=null;O("SUBSCRIBE_EMBED_HOVERCARD_URL")&&(kj(this),V(this.b,"mouseover",v(this.j,this)),V(this.b,"mouseout",v(this.W,this)),V(this.b,"click",v(this.W,this)),bg(Qg,za(this.f,!0),this),bg(Vg,za(this.f,!1),this),lj(this))}
function kj(a){var b={url:O("SUBSCRIBE_EMBED_HOVERCARD_URL"),style:"bubble",hideClickDetection:!0,show:!1,anchor:a.b,relayOpen:"-1"};a=v(a.g,a);Eg().open(b,a)}
function lj(a){aj()||Jf("LOGGED_IN",function(){this.D&&(this.W(),this.D.close(),this.D=null,kj(this))},a)}
jj.prototype.g=function(a){this.D=a;a=bj.v().isSubscribed(this.b);this.f(a)};
jj.prototype.j=function(){this.D&&this.D.restyle({show:!0})};
jj.prototype.W=function(){this.D&&this.D.restyle({show:!1})};
jj.prototype.f=function(a){if(this.D){a={isSubscribed:a};try{this.D.send("msg-hovercard-subscription",a,void 0,u("gapi.iframes.SAME_ORIGIN_IFRAMES_FILTER"))}catch(b){}}};function mj(){Dg(function(){var a=we(E("yt-subscribe"));a={width:a.width,height:a.height};var b=nj;Eg().ready(a,null,b)})}
function nj(a){if(a.length&&a[a.length-1]){a=a[a.length-1].eurl;var b=E("yt-subscribe"),c=bj.v();if(b=F(X(c),b))a&&(bj.v(),Nf(b,"parent-url",a)),new jj(b)}}
;function oj(a){R.call(this,1,arguments);this.b=a}
y(oj,R);function pj(a,b){R.call(this,2,arguments);this.f=a;this.b=b}
y(pj,R);function qj(a,b,c,d){R.call(this,1,arguments);this.b=b;this.f=c||null;this.itemId=d||null}
y(qj,R);function rj(a,b){R.call(this,1,arguments);this.f=a;this.b=b||null}
y(rj,R);function sj(a){R.call(this,1,arguments)}
y(sj,R);var tj=new S("ypc-core-load",oj),uj=new S("ypc-guide-sync-success",pj),vj=new S("ypc-purchase-success",qj),wj=new S("ypc-subscription-cancel",sj),xj=new S("ypc-subscription-cancel-success",rj),yj=new S("ypc-init-subscription",sj);var zj=!1,Aj=[];function Bj(a){a.b?zj?U(Rg,a):U(tj,new oj(function(){U(yj,new sj(a.b))})):Cj(a.f,a.j,a.g,a.source)}
function Dj(a){a.b?zj?U(Wg,a):U(tj,new oj(function(){U(wj,new sj(a.b))})):Ej(a.f,a.l,a.j,a.g,a.source)}
function Fj(a){Gj(Ka(a.b))}
function Hj(a){Ij(Ka(a.b))}
function Jj(a){Kj(a.g,a.f,a.b)}
function Lj(a){var b=a.itemId,c=a.b.subscriptionId;b&&c&&U(Qg,new Jg(b,c,a.b.channelInfo))}
function Mj(a){var b=a.b;Za(a.f,function(a,d){U(Qg,new Jg(d,a,b[d]))})}
function Nj(a){U(Vg,new Gg(a.f.itemId));a.b&&a.b.length&&(Oj(a.b,Vg),Oj(a.b,Xg))}
function Cj(a,b,c,d){var e=new Gg(a);U(Og,e);var f={};f.c=a;c&&(f.eurl=c);d&&(f.source=d);c={};(d=O("PLAYBACK_ID"))&&(c.plid=d);(d=O("EVENT_ID"))&&(c.ei=d);b&&Pj(b,c);xh("/subscription_ajax?action_create_subscription_to_channel=1",{method:"POST",Ha:f,L:c,onSuccess:function(b,c){var d=c.response;U(Qg,new Jg(a,d.id,d.channel_info));d.show_feed_privacy_dialog&&Q("SHOW-FEED-PRIVACY-SUBSCRIBE-DIALOG",a)},
ba:function(){U(Pg,e)}})}
function Ej(a,b,c,d,e){var f=new Gg(a);U(Tg,f);var g={};g.c=a;d&&(g.eurl=d);e&&(g.source=e);d={};d.c=a;d.s=b;(a=O("PLAYBACK_ID"))&&(d.plid=a);(a=O("EVENT_ID"))&&(d.ei=a);c&&Pj(c,d);xh("/subscription_ajax?action_remove_subscriptions=1",{method:"POST",Ha:g,L:d,onSuccess:function(){U(Vg,f)},
ba:function(){U(Ug,f)}})}
function Kj(a,b,c){if(a){var d={};d.channel_id=a;switch(b){case "receive-all-updates":d.receive_all_updates=!0;break;case "receive-no-updates":d.receive_no_updates=!0;d.receive_post_updates=!1;break;case "receive-highlight-updates":d.receive_all_updates=!1;d.receive_no_updates=!1;break;default:return}null===c||d.receive_no_updates||(d.receive_post_updates=c);var e=new Hg(a,b,c);xh("/subscription_ajax?action_update_subscription_preferences=1",{method:"POST",L:d,onError:function(){U(ah,e)},
onSuccess:function(){U($g,e)}})}}
function Gj(a){if(a.length){var b=Ma(a,0,40);U("subscription-batch-subscribe-loading");Oj(b,Og);var c={};c.a=b.join(",");var d=function(){U("subscription-batch-subscribe-loaded");Oj(b,Pg)};
xh("/subscription_ajax?action_create_subscription_to_all=1",{method:"POST",L:c,onSuccess:function(c,f){d();var e=f.response,h=e.id;if(qa(h)&&h.length==b.length){var l=e.channel_info_map;A(h,function(a,c){var d=b[c];U(Qg,new Jg(d,a,l[d]))});
a.length?Gj(a):U("subscription-batch-subscribe-finished")}},
onError:function(){d();U("subscription-batch-subscribe-failure")}})}}
function Ij(a){if(a.length){var b=Ma(a,0,40);U("subscription-batch-unsubscribe-loading");Oj(b,Tg);var c={};c.c=b.join(",");var d=function(){U("subscription-batch-unsubscribe-loaded");Oj(b,Ug)};
xh("/subscription_ajax?action_remove_subscriptions=1",{method:"POST",L:c,onSuccess:function(){d();Oj(b,Vg);a.length&&Ij(a)},
onError:function(){d()}})}}
function Oj(a,b){A(a,function(a){U(b,new Gg(a))})}
function Pj(a,b){var c=Cg(a),d;for(d in c)b[d]=c[d]}
;x("yt.setConfig",Cf);x("yt.config.set",Cf);x("ytbin.www.subscribeembed.init",function(){zj=!0;Aj.push(bg(Ng,Bj),bg(Sg,Dj));zj||Aj.push(bg(Rg,Bj),bg(Wg,Dj),bg(Lg,Fj),bg(Mg,Hj),bg(Zg,Jj),bg(vj,Lj),bg(xj,Nj),bg(uj,Mj));var a=bj.v(),b=X(a);b in Bg||(a.register(),yg(a,"yt-uix-init-"+b,a.init),yg(a,"yt-uix-dispose-"+b,a.dispose),Bg[b]=a);mj()});}).call(this);
