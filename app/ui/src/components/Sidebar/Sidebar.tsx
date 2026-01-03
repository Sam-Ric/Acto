import { useState } from 'react';
import './Sidebar.css';
import menu from '../../assets/menu.svg';
import home from '../../assets/home.svg';
import stats from '../../assets/stats.png';
import settings from '../../assets/settings.svg';

export default function Sidebar() {
    const [isExpanded, setIsExpanded] = useState(true);

    // Toggle sidebar visibility
    const toggleSidebar = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <>
            {/* Menu icon */}
            <img className="menu" src={menu} onClick={toggleSidebar} />
            <div className={`sidebar ${isExpanded ? 'expanded' : 'collapsed'}`}>
                {/* List of available pages */}
                <div className="pages">
                    {/* Home page */}
                    <a className={`home page ${isExpanded ? 'full' : 'minimal'}`} href="/">
                        <img src={home} />
                        <p>Home</p>
                    </a>
                    {/* Stats page */}
                    <a className={`stats page ${isExpanded ? 'full' : 'minimal'}`} href="/stats">
                        <img src={stats} />
                        <p>Stats</p>
                    </a>
                    {/* Settings page */}
                    <a className={`settings page ${isExpanded ? 'full' : 'minimal'}`} href="/settings">
                        <img src={settings} />
                        <p>Settings</p>
                    </a>
                </div>
            </div>
        </>
    );
}