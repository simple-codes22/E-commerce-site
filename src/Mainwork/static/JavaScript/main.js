const jumbotron = document.querySelector('.jumbo');
const content = document.getElementById('content');
const contentHead = document.querySelector('.content-head'),
      contentMain = document.querySelector('.content-main');
const individualCategory = document.getElementById('individ-cat');
const demoProduct = document.getElementById('demos');
let count = 0;
let contentsShowcase = [
    {
        'img': "../static/images/Showcase/Clothing-6.jpg",
        'head': 'Awesome Kicks',
        'main': 'Shop the shoes you desire to have.',
        'color': 'var(--shoes)'
    }, {
        'img': "../static/images/Showcase/Gaming-1.jpg",
        'head': 'Game 24/7',
        'main': 'Get the best gaming gadgets for am immersive experience.',
        'color': 'var(--gaming)'
    }, {
        'img': "../static/images/Showcase/Interior-2.jpg",
        'head': 'Beautify Your Home',
        'main': 'Tush up your home with amazing materials',
        'color': 'var(--shoes)'
    }, {
        'img': '../static/images/Showcase/Landscape-1.jpg',
        'head': "Nature's beauty",
        'main': "Experience the beauty of the outside world",
        'color': 'var(--green)'
    }, {
        'img': '../static/images/Showcase/Tech-5.jpg',
        'head': "Tech savvy you!!",
        'main': "Get the best of new tech gadgets",
        'color': 'var(--extra)'
    }
]

let jumbo = setInterval(function nextJumbo() {
    count >= contentsShowcase.length-1 ? count = 0 : count += 1;
    let current = contentsShowcase[count];
    console.log(current['color'])
    content.style.color = `${current['color']}`;
    jumbotron.style.background = `url("${current['img']}") no-repeat fixed center`;
    jumbotron.style.backgroundSize = "cover";
    contentHead.textContent = current['head'];
    contentMain.textContent = current["main"];
}, 5000);
