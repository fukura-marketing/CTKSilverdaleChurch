function debug () {

    if ( window.location.hostname === '127.0.0.1' ) {

        return true;

    }

}

class InfieldLabel {

    constructor () {

        this.inputs = document.querySelectorAll( '.infieldLabel .input' );
        this.setup();

        if ( debug() ) {

            console.log( 'DEBUG :: InfieldLabel Started' );

        }

    }

    setup () {

        let _this = this;

        _this.inputs.forEach( ( input ) => {

            input.addEventListener( 'blur', () => {

                if ( input.value.length > 0 && !input.classList.contains( 'mod-filled' ) ) {

                    input.classList.add( 'mod-filled' );

                } else if ( input.value.length === 0 && input.classList.contains( 'mod-filled' ) ) {

                    input.classList.remove( 'mod-filled' );

                }

            } );

        } );

    }

}

let tests = [
    [ '.infieldLabel', InfieldLabel, ],
];

for( let i = 0; i < tests.length; i++ ) {

    if ( document.querySelector( tests[ i ][ 0 ] ) ) {

        console.log( 'Started task :: ' + tests[ i ][ 0 ] );
        new tests[ i ][ 1 ]();

    }

}

if ( window.innerWidth <= 768 ) {

    let topnav = document.querySelectorAll( '.navigation-top-item-target' ),
        navlauncher = document.querySelector( '.navigation-top-launcher' ),
        container = document.querySelector( '.masthead-nav' ),
        list = document.querySelector( '.navigation-top' );

    topnav.forEach( ( nav ) => {

        nav.addEventListener( 'click', ( e ) => {

            e.preventDefault();

            topnav.forEach( ( siblingnav ) => {

                siblingnav.classList.remove( 'is-active' );

            } );

            nav.classList.add( 'is-active' );
            container.style.height = `${list.getBoundingClientRect().height}px`;
            return false;

        } );

    } );
    navlauncher.addEventListener( 'click', () => {

        if ( navlauncher.classList.contains( 'is-active' ) ) {

            navlauncher.classList.remove( 'is-active' );
            list.style.opacity = '0';

            container.style.height = `0`;

            setTimeout( () => {

                container.classList.remove( 'is-active' );
                container.removeAttribute( 'style' );
                list.removeAttribute( 'style' );

            }, 250 );

        } else {

            navlauncher.classList.add( 'is-active' );
            container.classList.add( 'is-active' );
            let h = list.getBoundingClientRect().height;
            container.style.height = '0';

            setTimeout( () => {

                container.style.opacity = '1';
                list.style.opacity = '1';
                container.style.height = `${h}px`;

            }, 50 );

        }

    } );

}

