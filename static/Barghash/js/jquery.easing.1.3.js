jQuery.easing.jswing=jQuery.easing.swing,jQuery.extend(jQuery.easing,{def:"easeOutQuad",swing:function(a,b,c,d,e){return jQuery.easing[jQuery.easing.def](a,b,c,d,e)},easeInQuad:function(e,a,b,c,d){return c*(a/=d)*a+b},easeOutQuad:function(e,a,b,c,d){return-c*(a/=d)*(a-2)+b},easeInOutQuad:function(e,a,b,c,d){return(a/=d/2)<1?c/2*a*a+b:-c/2*(--a*(a-2)-1)+b},easeInCubic:function(e,a,b,c,d){return c*(a/=d)*a*a+b},easeOutCubic:function(e,a,b,c,d){return c*((a=a/d-1)*a*a+1)+b},easeInOutCubic:function(e,a,b,c,d){return(a/=d/2)<1?c/2*a*a*a+b:c/2*((a-=2)*a*a+2)+b},easeInQuart:function(e,a,b,c,d){return c*(a/=d)*a*a*a+b},easeOutQuart:function(e,a,b,c,d){return-c*((a=a/d-1)*a*a*a-1)+b},easeInOutQuart:function(e,a,b,c,d){return(a/=d/2)<1?c/2*a*a*a*a+b:-c/2*((a-=2)*a*a*a-2)+b},easeInQuint:function(e,a,b,c,d){return c*(a/=d)*a*a*a*a+b},easeOutQuint:function(e,a,b,c,d){return c*((a=a/d-1)*a*a*a*a+1)+b},easeInOutQuint:function(e,a,b,c,d){return(a/=d/2)<1?c/2*a*a*a*a*a+b:c/2*((a-=2)*a*a*a*a+2)+b},easeInSine:function(e,b,c,a,d){return-a*Math.cos(b/d*(Math.PI/2))+a+c},easeOutSine:function(e,a,b,c,d){return c*Math.sin(a/d*(Math.PI/2))+b},easeInOutSine:function(e,a,b,c,d){return-c/2*(Math.cos(Math.PI*a/d)-1)+b},easeInExpo:function(e,a,b,c,d){return 0==a?b:c*Math.pow(2,10*(a/d-1))+b},easeOutExpo:function(e,a,b,c,d){return a==d?b+c:c*(-Math.pow(2,-10*a/d)+1)+b},easeInOutExpo:function(e,a,b,c,d){return 0==a?b:a==d?b+c:(a/=d/2)<1?c/2*Math.pow(2,10*(a-1))+b:c/2*(-Math.pow(2,-10* --a)+2)+b},easeInCirc:function(e,a,b,c,d){return-c*(Math.sqrt(1-(a/=d)*a)-1)+b},easeOutCirc:function(e,a,b,c,d){return c*Math.sqrt(1-(a=a/d-1)*a)+b},easeInOutCirc:function(e,a,b,c,d){return(a/=d/2)<1?-c/2*(Math.sqrt(1-a*a)-1)+b:c/2*(Math.sqrt(1-(a-=2)*a)+1)+b},easeInElastic:function(h,c,e,a,f){var g=1.70158,b=0,d=a;if(0==c)return e;if(1==(c/=f))return e+a;if(b||(b=.3*f),d<Math.abs(a)){d=a;var g=b/4}else var g=b/(2*Math.PI)*Math.asin(a/d);return-(d*Math.pow(2,10*(c-=1))*Math.sin((c*f-g)*(2*Math.PI)/b))+e},easeOutElastic:function(h,c,e,a,f){var g=1.70158,b=0,d=a;if(0==c)return e;if(1==(c/=f))return e+a;if(b||(b=.3*f),d<Math.abs(a)){d=a;var g=b/4}else var g=b/(2*Math.PI)*Math.asin(a/d);return d*Math.pow(2,-10*c)*Math.sin((c*f-g)*(2*Math.PI)/b)+a+e},easeInOutElastic:function(h,a,e,b,f){var g=1.70158,c=0,d=b;if(0==a)return e;if(2==(a/=f/2))return e+b;if(c||(c=f*(.3*1.5)),d<Math.abs(b)){d=b;var g=c/4}else var g=c/(2*Math.PI)*Math.asin(b/d);return a<1?-0.5*(d*Math.pow(2,10*(a-=1))*Math.sin((a*f-g)*(2*Math.PI)/c))+e:d*Math.pow(2,-10*(a-=1))*Math.sin((a*f-g)*(2*Math.PI)/c)*.5+b+e},easeInBack:function(f,b,c,d,e,a){return void 0==a&&(a=1.70158),d*(b/=e)*b*((a+1)*b-a)+c},easeOutBack:function(f,a,c,d,e,b){return void 0==b&&(b=1.70158),d*((a=a/e-1)*a*((b+1)*a+b)+1)+c},easeInOutBack:function(f,a,c,d,e,b){return(void 0==b&&(b=1.70158),(a/=e/2)<1)?d/2*(a*a*(((b*=1.525)+1)*a-b))+c:d/2*((a-=2)*a*(((b*=1.525)+1)*a+b)+2)+c},easeInBounce:function(c,d,e,a,b){return a-jQuery.easing.easeOutBounce(c,b-d,0,a,b)+e},easeOutBounce:function(e,a,b,c,d){return(a/=d)<1/2.75?c*(7.5625*a*a)+b:a<2/2.75?c*(7.5625*(a-=1.5/2.75)*a+.75)+b:a<2.5/2.75?c*(7.5625*(a-=2.25/2.75)*a+.9375)+b:c*(7.5625*(a-=2.625/2.75)*a+.984375)+b},easeInOutBounce:function(d,b,e,c,a){return b<a/2?.5*jQuery.easing.easeInBounce(d,2*b,0,c,a)+e:.5*jQuery.easing.easeOutBounce(d,2*b-a,0,c,a)+.5*c+e}})