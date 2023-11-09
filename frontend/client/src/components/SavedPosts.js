import React from 'react'

function SavedPosts() {
    const images = [{"img": "https://media.self.com/photos/5f0885ffef7a10ffa6640daa/4:3/w_5240,h_3929,c_limit/travel_plane_corona.jpeg"},{"img": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dHJhdmVsJTIwd2FsbHBhcGVyfGVufDB8fDB8fHww"},{"img": "https://assets.weforum.org/article/image/fhwx9sNtvefClbbL-r7qlEYDStVj_bjqkXK8q6EhjcM.jpg"}, {"img": "https://media.istockphoto.com/id/1368808461/photo/young-woman-feeding-fish-on-tropical-beach.jpg?s=612x612&w=0&k=20&c=qIdzSEI3BQvGliysV65R5NzHGuhX_4Mq_PU7nBhhsBQ="}]
  
    return (
    <div className='img-grid'>{images.map(image => (<img className="" src={images.img} alt=""/>))}</div>
  )
}

export default SavedPosts