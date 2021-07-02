odoo.define('hello_world.main', function (require) {
    // console.log('hello javascript')
    const AbstractAction = require('web.AbstractAction');
    // console.log(AbstractAction);
    const core = require('web.core');
    // Defines a widget named "HelloWorldAction"
    const HelloWorldAction = AbstractAction.extend({
        //start: function () {
        //    this.$el.html('hello');
        //}
        // Use "hello_world.ClientAction" template
        template: "hello_world.ClientAction",
        info: "This message comes from the JS"
    });
    // Registry "HelloWorldAction" action
    core.action_registry.add('hello_world.action', HelloWorldAction);
});
