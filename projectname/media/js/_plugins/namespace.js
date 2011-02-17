/// Create the Namespace Manager that we'll use to
/// make creating namespaces a little easier.

(function() {
    if (typeof window.namespace == 'undefined') {
        window.namespace = {
            register: function(ns){
                ns = ns.split('.');

                if (!window[ns[0]]) {
                    window[ns[0]] = {};
                }
                
                var full_ns = ns[0];
                for (var i = 1; i < ns.length; i++) {
                    full_ns += "." + ns[i];
                    eval("if (!window." + full_ns + ") { window." + full_ns + "={}; }");
                }
            }
        };
    }
})();