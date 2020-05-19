// Start with first post.
let counter = 1;

// Load posts 6 at a time.
const quantity = 6;

// When DOM loads, render the first 6 posts.
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 6 posts.
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Load next set of posts.
function load() {
    // Set start and end post numbers, and update counter.
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Open new request to get new posts.
    const request = new XMLHttpRequest();
    request.open('POST', '/posts');
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        data.forEach(add_post);
    };

    // Add start and end points to request data.
    const data = new FormData();
    data.append('start', start);
    data.append('end', end);

    // Send request.
    request.send(data);
};

// Add a new post with given contents to DOM.
function add_post(contents) {

    const col = document.createElement('div');
    col.className = 'col-md-4 col-sm-6 col-12';
    col.style = 'margin-bottom: 15px;';

    // Create new post.
    const post = document.createElement('div');
    post.className = 'card';
    //post.innerHTML = contents;
    post.style = "height: 400px;"
    // post.style = "max-width: 140rem;"

    const post_img = document.createElement('img')
    post_img.className = 'card-img-top'
    post_img.src = "https://images.foody.vn/res/g15/147556/prof/s640x400/foody-mobile-gogi-house-dn1-mb-jp-611-635787900703764814.jpg"
    post_img.alt = "Card image cap"

    const post_card = document.createElement('div')
    post_card.className = "card-body"

    const h5 = document.createElement('h5')
    h5.className = "card-title"
    // h5.innerHTML = "Name restaurant"
    h5.innerHTML = contents;

    const prate = document.createElement('p')
    prate.className = "card-text"
    prate.innerHTML = "Rating"

    post_card.append(h5)
    post_card.append(prate)

    post.append(post_img)
    post.append(post_card)
    
    col.append(post);
    // Add post to DOM.
    document.querySelector('#cardpost').append(col);
    document.querySelector('#cardpost').append(document.createElement('br'));
};