 // modalを出す
 const modalOpen = document.querySelectorAll( '.modal-open' );
 const modal = document.querySelectorAll( '.modal' );
 const modalCover = document.querySelectorAll( '.modal-cover' );

 let modalCloseAction;
 let dataModalOpen;
 let targetModal;

 const TIMEOUT_SPEED = 500;

 for ( let i = 0; i < modalOpen.length; i++ ) {

     //モーダルを下げる処理
     modalCloseAction = function ( e ) {
         targetModal = e.currentTarget.closest( '.modal' );
         targetModal.classList.add( 'is-close' );

         setTimeout( function ( e ) {
             targetModal.classList.remove( 'is-open' );
             targetModal.classList.remove( 'is-close' );
         }, TIMEOUT_SPEED );
     };

     // グレー部分をクリックでmodalを下げる
     const modalWrapClose = function () {
         modalCover[ i ].addEventListener( 'click', function ( e ) {
             modalCloseAction( e );
         }, false );
     };

     // modalをあげる
     const modalWrapOpen = function ( e ) {
         dataModalOpen = e.currentTarget.getAttribute( 'data-modal-open' );
         for ( var b = 0; b < modal.length; b++ ) {

             if ( modal[ b ].getAttribute( 'data-modal' ) === dataModalOpen ) {
                 modal[ b ].classList.add( 'is-open' );
                 modalWrapClose();
                 return false;
             }
         }
     };

     modalOpen[ i ].addEventListener( 'click', function ( e ) {
         modalWrapOpen( e );
     }, false );
 }

 // modalを下げる
 const modalBtnClose = document.querySelectorAll( '.btn-close' );
 for ( let n = 0; n < modalBtnClose.length; n++ ) {
     modalBtnClose[ n ].addEventListener( 'click', function ( e ) {
         modalCloseAction( e );
         return false;
     }, false );
 }



//  メニューボタン
document.querySelector( '.nav-button' ).addEventListener( 'click', function () {
    document.querySelector( '.nav-button' ).classList.toggle( 'active' );
    document.querySelector( '.sidebar' ).classList.toggle( 'is-open' );
} );

document.querySelector( '.accordion' ).addEventListener( 'click', function () {
    this.classList.toggle( "is-active" );
} );

document.querySelector( '.accordion1' ).addEventListener( 'click', function () {
    this.classList.toggle( "is-active" );
} );

document.querySelector( '.sidebar-close' ).addEventListener( 'click', function () {
    document.querySelector( '.sidebar' ).classList.remove( 'is-open' );
} );
