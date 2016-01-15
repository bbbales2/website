var Main = Main || {}

Main.Controller = Backbone.View.extend(
    {
        events : {
        },

        initialize : function(options)
        {
            this.start = 0;
        },

        render : function()
        {
            this.$el = $("body");
            this.el = this.$el[0];

            var eqs = this.$el.find( '.eq' );

            for(var i = 0; i < eqs.length; i++)
            {
                var eq = eqs.eq(i);

                var text = eq.text();

                eq.empty();

                var number = $( '<span class="eqNumber">&#40;' + i + '&#41; </span>' ).appendTo( eq )
                var tex = $( '<span></span>' ).appendTo( eq );

                katex.render(text, tex[0]);
            }

            var refs = this.$el.find( 'a.ref' );

            for(var i = 0; i < refs; i++)
            {
                ref.data('ref');
            }

            this.delegateEvents();
        },
    }
);

$( document ).ready( function() {
    var cont = new Main.Controller();
    
    cont.render();
});

