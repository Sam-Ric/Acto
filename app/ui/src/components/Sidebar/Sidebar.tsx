import './Sidebar.css';
import menu from '../../assets/menu.svg';
import home from '../../assets/home.svg';
import stats from '../../assets/stats.png';
import settings from '../../assets/settings.svg';
import { useSidebar } from '../../components/SidebarContext';
import { Link } from 'react-router-dom';

export default function Sidebar() {
    const { isSidebarExpanded, toggleSidebar } = useSidebar();

    return (
        <>
            {/* Menu icon */}
            <img className="menu" src={menu} onClick={toggleSidebar} />
            <div className={`sidebar ${isSidebarExpanded ? 'expanded' : 'collapsed'}`}>
                {/* List of available pages */}
                <div className="pages">
                    {/* Home page */}
                    <Link className={`page ${isSidebarExpanded ? 'full' : 'minimal'}`} to="/">
                        <img src={home} />
                        <p>Home</p>
                    </Link>
                    {/* Stats page */}
                    <Link className={`page ${isSidebarExpanded ? 'full' : 'minimal'}`} to="/stats">
                        <img src={stats} />
                        <p>Stats</p>
                    </Link>
                    {/* Settings page */}
                    <Link className={`page ${isSidebarExpanded ? 'full' : 'minimal'}`} to="/settings">
                        <img src={settings} />
                        <p>Settings</p>
                    </Link>
                </div>
            </div>
        </>
    );
}