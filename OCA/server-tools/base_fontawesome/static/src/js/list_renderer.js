odoo.define("base_fontawesome5.ListRenderer", function(require) {
    "use strict";

    var ListRenderer = require("web.ListRenderer");

    ListRenderer.include({
        _renderButton: function(record, node) {
            var $button = this._super.apply(this, arguments);

            if (node.attrs.brand_icon) {
                $("<div>")
                    .addClass("fab fa-fw o_button_icon")
                    .addClass(node.attrs.brand_icon)
                    .prependTo($button);
            }
            if (node.attrs.solid_icon) {
                $("<div>")
                    .addClass("fas fa-fw o_button_icon")
                    .addClass(node.attrs.solid_icon)
                    .prependTo($button);
            }
            if (node.attrs.regular_icon) {
                $("<div>")
                    .addClass("far fa-fw o_button_icon")
                    .addClass(node.attrs.regular_icon)
                    .prependTo($button);
            }
            return $button;
        },
    });
});
