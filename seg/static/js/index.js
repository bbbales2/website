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
            var refNumbers = {};

            for(var i = 0; i < refs.length; i++)
            {
                var ref = refs.eq(i);
                var refName = ref.data('ref');

                var target = $( '.' + refName );

                if(!(refName in refNumbers))
                {
                    refNumbers[refName] = _.keys(refNumbers).length;

                    $( '<a name="' + refName + '"></a>' ).prependTo( target );
                    $( '<span>Figure ' + refNumbers[refName] + ': </span>' ).prependTo( target.find( '.caption' ) );
                }

                ref.text( 'Figure ' + refNumbers[refName] );

                ref.prop('href', '#' + refName);
            }

            this.delegateEvents();
        },
    }
);

$( document ).ready( function() {
    var cont = new Main.Controller();
    
    cont.render();
});

