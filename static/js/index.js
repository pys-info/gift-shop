        let thumbnails = document.getElementsByClassName('thumbnail')
        let activeImages = document.getElementsByClassName('active')
        for (var i=0; i < thumbnails.length; i++){
            thumbnails[i].addEventListener('click', function(){
                if (activeImages.length > 0){
                    activeImages[0].classList.remove('active')
                }
                this.className += " active";
                document.getElementById('featured').src = this.src;
            })
        }



