function Drawer(el, open = false) { // A 
    var a = false;
    this.el = el;
    this.isOpen = open;
    Object.assign(this.el.style, {
        display: 'block', 
        position: 'fixed',
        top: 0,
        bottom: 0,
        left: 0,
        width: '200px',
        padding: '10px',
        backgroundColor: 'white',
        boxShadow: '0 0 36px 0 rgba(0,0,0,0.1)',
        transition: 'all 0.2s ease-out' 
    });
    (this.isOpen) ? this.open() : this.close();
    }

    Drawer.prototype.open = function() {  // B 
    this.isOpen = true;
    this.el.style.transform = 'translate(0px)'; 
    }
    Drawer.prototype.close = function() { 
    this.isOpen = false;
    this.el.style.transform = 'translate(-220px)'; 
    }

    const sideMenu = new Drawer(document.querySelector('.drawer')); // C
    opners = document.getElementsByClassName('drawer-opener');
    
    for (const element of opners) {
        element.addEventListener('click', e => {  
        (!sideMenu.isOpen) ? sideMenu.open() : sideMenu.close();
    });
    }
