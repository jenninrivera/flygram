import React from 'react'
import "./CrashPadPostCard.css"
function CrashPadPostCard({crashpadposts}) {
  
  return (
    // <div className="crashpost">

    //     <div className="user_info">
    //         <div id="propic">
    //             <img src="" alt=""/>
    //         </div>
    //         <span>username</span>
    //     </div>
    //     <h3>📍 location</h3>
    //     <p>text</p>
    // </div>
    <>
    <div class="blog-container">
    
    <div class="blog-header">
        <div class="blog-author--no-cover">
            <h3>{crashpadposts.username}</h3>
        </div>
    </div>

    <div class="blog-body">
        <div class="blog-title">
        <h1><a href="#">📍 {crashpadposts.location}</a></h1>
        </div>
        <div class="blog-summary">
        <p>{crashpadposts.text}</p>
        </div>
    </div>
    </div>
    </>

  )
}


export default CrashPadPostCard