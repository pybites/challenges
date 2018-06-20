(function(){var h=this;function k(a){return"string"==typeof a}
function aa(a){a=a.split(".");for(var b=h,c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function m(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
;var ba=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(k(a))return k(b)&&1==b.length?a.indexOf(b,0):-1;
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},ca=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f=k(a)?a.split(""):a,g=0;g<c;g++)if(g in f){var l=f[g];
b.call(void 0,l,g,a)&&(d[e++]=l)}return d};
function da(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c],e=m(d);if("array"==e||"object"==e&&"number"==typeof d.length){e=a.length||0;var f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;var p;a:{var ea=h.navigator;if(ea){var fa=ea.userAgent;if(fa){p=fa;break a}}p=""};var ha="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function ia(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<ha.length;f++)c=ha[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var ja=-1!=p.indexOf("Trident")||-1!=p.indexOf("MSIE"),ka=-1!=p.toLowerCase().indexOf("webkit")&&-1==p.indexOf("Edge");function r(a,b){this.width=a;this.height=b}
r.prototype.aspectRatio=function(){return this.width/this.height};
r.prototype.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
r.prototype.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
r.prototype.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function la(){var a=document;return k("yt-subscribe-card")?a.getElementById("yt-subscribe-card"):"yt-subscribe-card"}
;/*
 gapi.loader.OBJECT_CREATE_TEST_OVERRIDE &&*/
var t=window,w=document,ma=t.location;function na(){}
var oa=/\[native code\]/;function x(a,b,c){return a[b]=a[b]||c}
function pa(a){a=a.sort();for(var b=[],c=void 0,d=0;d<a.length;d++){var e=a[d];e!=c&&b.push(e);c=e}return b}
function y(){var a;if((a=Object.create)&&oa.test(a))a=a(null);else{a={};for(var b in a)a[b]=void 0}return a}
var z=x(t,"gapi",{});var A;A=x(t,"___jsl",y());x(A,"I",0);x(A,"hel",10);function qa(){var a=ma.href;if(A.dpo)var b=A.h;else{b=A.h;var c=RegExp("([#].*&|[#])jsh=([^&#]*)","g"),d=RegExp("([?#].*&|[?#])jsh=([^&#]*)","g");if(a=a&&(c.exec(a)||d.exec(a)))try{b=decodeURIComponent(a[2])}catch(e){}}return b}
function ra(a){var b=x(A,"PQ",[]);A.PQ=[];var c=b.length;if(0===c)a();else for(var d=0,e=function(){++d===c&&a()},f=0;f<c;f++)b[f](e)}
function B(a){return x(x(A,"H",y()),a,y())}
;var F=x(A,"perf",y());x(F,"g",y());var sa=x(F,"i",y());x(F,"r",[]);y();y();function G(a,b,c){b&&0<b.length&&(b=ta(b),c&&0<c.length&&(b+="___"+ta(c)),28<b.length&&(b=b.substr(0,28)+(b.length-28)),c=b,b=x(sa,"_p",y()),x(b,c,y())[a]=(new Date).getTime(),b=F.r,"function"===typeof b?b(a,"_p",c):b.push([a,"_p",c]))}
function ta(a){return a.join("__").replace(/\./g,"_").replace(/\-/g,"_").replace(/,/g,"_")}
;var ua=y(),H=[];function J(a){throw Error("Bad hint"+(a?": "+a:""));}
H.push(["jsl",function(a){for(var b in a)if(Object.prototype.hasOwnProperty.call(a,b)){var c=a[b];"object"==typeof c?A[b]=x(A,b,[]).concat(c):x(A,b,c)}if(b=a.u)a=x(A,"us",[]),a.push(b),(b=/^https:(.*)$/.exec(b))&&a.push("http:"+b[1])}]);
var va=/^(\/[a-zA-Z0-9_\-]+)+$/,wa=[/\/amp\//,/\/amp$/,/^\/amp$/],xa=/^[a-zA-Z0-9\-_\.,!]+$/,ya=/^gapi\.loaded_[0-9]+$/,za=/^[a-zA-Z0-9,._-]+$/;function Aa(a,b,c,d){var e=a.split(";"),f=e.shift(),g=ua[f],l=null;g?l=g(e,b,c,d):J("no hint processor for: "+f);l||J("failed to generate load url");b=l;c=b.match(Ba);(d=b.match(Ca))&&1===d.length&&Da.test(b)&&c&&1===c.length||J("failed sanity: "+a);return l}
function Ea(a,b,c,d){function e(a){return encodeURIComponent(a).replace(/%2C/g,",")}
a=Fa(a);ya.test(c)||J("invalid_callback");b=Ga(b);d=d&&d.length?Ga(d):null;return[encodeURIComponent(a.pathPrefix).replace(/%2C/g,",").replace(/%2F/g,"/"),"/k=",e(a.version),"/m=",e(b),d?"/exm="+e(d):"","/rt=j/sv=1/d=1/ed=1",a.a?"/am="+e(a.a):"",a.c?"/rs="+e(a.c):"",a.f?"/t="+e(a.f):"","/cb=",e(c)].join("")}
function Fa(a){"/"!==a.charAt(0)&&J("relative path");for(var b=a.substring(1).split("/"),c=[];b.length;){a=b.shift();if(!a.length||0==a.indexOf("."))J("empty/relative directory");else if(0<a.indexOf("=")){b.unshift(a);break}c.push(a)}a={};for(var d=0,e=b.length;d<e;++d){var f=b[d].split("="),g=decodeURIComponent(f[0]),l=decodeURIComponent(f[1]);2==f.length&&g&&l&&(a[g]=a[g]||l)}b="/"+c.join("/");va.test(b)||J("invalid_prefix");c=0;for(d=wa.length;c<d;++c)wa[c].test(b)&&J("invalid_prefix");c=K(a,"k",
!0);d=K(a,"am");e=K(a,"rs");a=K(a,"t");return{pathPrefix:b,version:c,a:d,c:e,f:a}}
function Ga(a){for(var b=[],c=0,d=a.length;c<d;++c){var e=a[c].replace(/\./g,"_").replace(/-/g,"_");za.test(e)&&b.push(e)}return b.join(",")}
function K(a,b,c){a=a[b];!a&&c&&J("missing: "+b);if(a){if(xa.test(a))return a;J("invalid: "+b)}return null}
var Da=/^https?:\/\/[a-z0-9_.-]+\.google(rs)?\.com(:\d+)?\/[a-zA-Z0-9_.,!=\-\/]+$/,Ca=/\/cb=/g,Ba=/\/\//g;function Ha(){var a=qa();if(!a)throw Error("Bad hint");return a}
ua.m=function(a,b,c,d){(a=a[0])||J("missing_hint");return"https://apis.google.com"+Ea(a,b,c,d)};
var L=decodeURI("%73cript"),Ia=/^[-+_0-9\/A-Za-z]+={0,2}$/;function Ja(a,b){for(var c=[],d=0;d<a.length;++d){var e=a[d],f;if(f=e){a:{for(f=0;f<b.length;f++)if(b[f]===e)break a;f=-1}f=0>f}f&&c.push(e)}return c}
function Ka(){var a=A.nonce;return void 0!==a?a&&a===String(a)&&a.match(Ia)?a:A.nonce=null:w.querySelector?(a=w.querySelector("script[nonce]"))?(a=a.nonce||a.getAttribute("nonce")||"",a&&a===String(a)&&a.match(Ia)?A.nonce=a:A.nonce=null):null:null}
function La(a){if("loading"!=w.readyState)Ma(a);else{var b=Ka(),c="";null!==b&&(c=' nonce="'+b+'"');w.write("<"+L+' src="'+encodeURI(a)+'"'+c+"></"+L+">")}}
function Ma(a){var b=w.createElement(L);b.setAttribute("src",a);a=Ka();null!==a&&b.setAttribute("nonce",a);b.async="true";(a=w.getElementsByTagName(L)[0])?a.parentNode.insertBefore(b,a):(w.head||w.body||w.documentElement).appendChild(b)}
function Na(a,b){var c=b&&b._c;if(c)for(var d=0;d<H.length;d++){var e=H[d][0],f=H[d][1];f&&Object.prototype.hasOwnProperty.call(c,e)&&f(c[e],a,b)}}
function Oa(a,b,c){Pa(function(){var c=b===qa()?x(z,"_",y()):y();c=x(B(b),"_",c);a(c)},c)}
function M(a,b){var c=b||{};"function"==typeof b&&(c={},c.callback=b);Na(a,c);var d=a?a.split(":"):[],e=c.h||Ha(),f=x(A,"ah",y());if(f["::"]&&d.length){for(var g=[],l=null;l=d.shift();){var n=l.split(".");n=f[l]||f[n[1]&&"ns:"+n[0]||""]||e;var C=g.length&&g[g.length-1]||null,D=C;C&&C.hint==n||(D={hint:n,b:[]},g.push(D));D.b.push(l)}var I=g.length;if(1<I){var E=c.callback;E&&(c.callback=function(){0==--I&&E()})}for(;d=g.shift();)Qa(d.b,c,d.hint)}else Qa(d||[],c,e)}
function Qa(a,b,c){function d(a,b){if(I)return 0;t.clearTimeout(D);E.push.apply(E,q);var d=((z||{}).config||{}).update;d?d(f):f&&x(A,"cu",[]).push(f);if(b){G("me0",a,R);try{Oa(b,c,C)}finally{G("me1",a,R)}}return 1}
a=pa(a)||[];var e=b.callback,f=b.config,g=b.timeout,l=b.ontimeout,n=b.onerror,C=void 0;"function"==typeof n&&(C=n);var D=null,I=!1;if(g&&!l||!g&&l)throw"Timeout requires both the timeout parameter and ontimeout parameter to be set";n=x(B(c),"r",[]).sort();var E=x(B(c),"L",[]).sort(),R=[].concat(n);0<g&&(D=t.setTimeout(function(){I=!0;l()},g));
var q=Ja(a,E);if(q.length){q=Ja(a,n);var u=x(A,"CP",[]),v=u.length;u[v]=function(a){function b(){var a=u[v+1];a&&a()}
function c(b){u[v]=null;d(q,a)&&ra(function(){e&&e();b()})}
if(!a)return 0;G("ml1",q,R);0<v&&u[v-1]?u[v]=function(){c(b)}:c(b)};
if(q.length){var Z="loaded_"+A.I++;z[Z]=function(a){u[v](a);z[Z]=null};
a=Aa(c,q,"gapi."+Z,n);n.push.apply(n,q);G("ml0",q,R);b.sync||t.___gapisync?La(a):Ma(a)}else u[v](na)}else d(q)&&e&&e()}
function Pa(a,b){if(A.hee&&0<A.hel)try{return a()}catch(c){b&&b(c),A.hel--,M("debug_error",function(){try{window.___jsl.hefn(c)}catch(d){throw c;}})}else try{return a()}catch(c){throw b&&b(c),c;
}}
z.load=function(a,b){return Pa(function(){return M(a,b)})};function Ra(a){if(a.classList)return a.classList;a=a.className;return k(a)&&a.match(/\S+/g)||[]}
function Sa(a,b){if(a.classList)var c=a.classList.contains(b);else c=Ra(a),c=0<=ba(c,b);return c}
function Ta(a,b){a.classList?a.classList.add(b):Sa(a,b)||(a.className+=0<a.className.length?" "+b:b)}
function Ua(a,b){a.classList?a.classList.remove(b):Sa(a,b)&&(a.className=ca(Ra(a),function(a){return a!=b}).join(" "))}
;function Va(a){var b=a.offsetWidth,c=a.offsetHeight,d=ka&&!b&&!c;if((void 0===b||d)&&a.getBoundingClientRect){a:{try{var e=a.getBoundingClientRect()}catch(f){e={left:0,top:0,right:0,bottom:0};break a}ja&&a.ownerDocument.body&&(a=a.ownerDocument,e.left-=a.documentElement.clientLeft+a.body.clientLeft,e.top-=a.documentElement.clientTop+a.body.clientTop)}return new r(e.right-e.left,e.bottom-e.top)}return new r(b,c)}
;var N=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{},O=["yt","config_"],P=h;O[0]in P||"undefined"==typeof P.execScript||P.execScript("var "+O[0]);for(var Q;O.length&&(Q=O.shift());)O.length||void 0===N?P[Q]&&P[Q]!==Object.prototype[Q]?P=P[Q]:P=P[Q]={}:P[Q]=N;function Wa(){return aa("gapi.iframes.getContext")()}
function Xa(){return aa("gapi.iframes.SAME_ORIGIN_IFRAMES_FILTER")}
;function Ya(a){try{a.register("msg-hovercard-subscription",Za,Xa())}catch(b){}}
function Za(a){if(a){a=!!a.isSubscribed;var b=la();a?Ua(b,"subscribe"):Ta(b,"subscribe");a?Ta(b,"subscribed"):Ua(b,"subscribed")}}
;function S(){var a=la();b:{var b=9==a.nodeType?a:a.ownerDocument||a.document;if(b.defaultView&&b.defaultView.getComputedStyle&&(b=b.defaultView.getComputedStyle(a,null))){b=b.display||b.getPropertyValue("display")||"";break b}b=""}if("none"!=(b||(a.currentStyle?a.currentStyle.display:null)||a.style&&a.style.display))a=Va(a);else{b=a.style;var c=b.display,d=b.visibility,e=b.position;b.visibility="hidden";b.position="absolute";b.display="inline";a=Va(a);b.display=c;b.position=e;b.visibility=d}a={width:a.width,
height:a.height};Wa().ready(a,null,void 0);a=Xa();Wa().addOnOpenerHandler(Ya,null,a)}
var T=S;T=void 0===T?{}:T;"function"==m(T)&&(T={callback:T});S=T;
if(S.gapiHintOverride||"GAPI_HINT_OVERRIDE"in N&&N.GAPI_HINT_OVERRIDE){var $a;var U=document.location.href;if(-1!=U.indexOf("?")){U=(U||"").split("#")[0];var ab=U.split("?",2),V=1<ab.length?ab[1]:ab[0];"?"==V.charAt(0)&&(V=V.substr(1));for(var bb=V.split("&"),W={},cb=0,db=bb.length;cb<db;cb++){var X=bb[cb].split("=");if(1==X.length&&X[0]||2==X.length){var Y=decodeURIComponent((X[0]||"").replace(/\+/g," ")),eb=decodeURIComponent((X[1]||"").replace(/\+/g," "));Y in W?"array"==m(W[Y])?da(W[Y],eb):W[Y]=
[W[Y],eb]:W[Y]=eb}}$a=W}else $a={};var fb=$a.gapi_jsh;fb&&ia(S,{_c:{jsl:{h:fb}}})}M("gapi.iframes:gapi.iframes.style.common",S);}).call(this);
