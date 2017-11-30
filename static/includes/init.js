
// load common code that includes config, then load the app logic for this page.
requirejs(['./common'], function(common){
    requirejs(['{{ url_of("static",filename="./includes/app/main") }}']);
});
