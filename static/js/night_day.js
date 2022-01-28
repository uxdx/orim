function daynighthandle(self){
    var target = document.querySelector('body');
    if(self.value == 'dark'){
        target.style.backgroundColor = 'black';
        target.style.color = 'white';
        document.querySelector('button').style.backgroundColor = 'black';
        document.querySelector('button').style.color = 'white';
        document.querySelector('.drawer').style.backgroundColor = 'gray';
        document.querySelector('.drawer button').style.backgroundColor = 'gray';
        document.querySelector('.drawer button').style.color = 'white';
        self.value = 'white';
    } else {
        target.style.backgroundColor = 'white';
        target.style.color = 'black';
        document.querySelector('button').style.backgroundColor = 'white';
        document.querySelector('button').style.color = 'black';
        document.querySelector('.drawer').style.backgroundColor = 'white';
        document.querySelector('.drawer button').style.backgroundColor = 'white';
        document.querySelector('.drawer button').style.color = 'black';
        self.value = 'dark';
    }
}