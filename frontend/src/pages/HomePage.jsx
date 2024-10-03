import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchStories } from '../features/stories/storySlice';
import { Link, useNavigate } from 'react-router-dom'; // Import useNavigate
import '../css/homepage.css';

const HomePage = () => {
    const dispatch = useDispatch();
    const stories = useSelector((state) => state.stories.stories);
    const status = useSelector((state) => state.stories.status);
    const navigate = useNavigate(); // Initialize useNavigate

    useEffect(() => {
        dispatch(fetchStories());
    }, [dispatch]);

    const handleCreateStoryClick = () => {
        navigate('/create-story'); // Navigate to create story page
    };

    return (
        <main>
            <div className="story-title">
                <h1>Stories</h1>
                <button onClick={handleCreateStoryClick} className="create-story-btn">
                    + Create your own story
                </button>
            </div>
            {status === 'loading' && <p>Loading...</p>}
            {status === 'failed' && <p>Please Login to see stories</p>}
            <ul className='cards'>
                {stories?.map((story) => (
                    <li key={story.id} className="card-container">
                        <Link to={`story/${story.id}`} className="card">
                            <div className="story-box">
                                <img src={story.image} alt={story.title} className="story-image" />
                            </div>
                            <span className="title">{story.title}</span>
                            <span className="status">
                                <b>Completed</b>: {story.completed ? <span>⦿</span> : <span>⦾</span>}
                            </span>
                            <span className="author"><b>Creator</b>: {story.author.username}</span>
                        </Link>
                    </li>
                ))}
            </ul>
        </main>
    );
};

export default HomePage;
