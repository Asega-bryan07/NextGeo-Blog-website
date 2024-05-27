const likeIcon = document.getElementById('like-icon') as HTMLElement;
const likeCount = document.getElementById('like-count') as HTMLElement;

likeIcon.onclick = () => {
    const blogId = likeIcon.getAttribute('data-blog');
    const url = `/like_blog/${parseInt(blogId)}/`;
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.liked) {
            likeIcon.classList.remove('empty-heart');
        } else {
            likeIcon.classList.add('empty-heart');
        }
        likeCount.innerHTML = data.like_count.toString(); // Ensure like_count is a string
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
};
