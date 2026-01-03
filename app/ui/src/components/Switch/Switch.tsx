import { useState } from "react";
import "./Switch.css";

interface SwitchParams {
    onToggle: (status: boolean) => void;
    size?: string;
};

export default function Switch({ onToggle, size = "8rem" }: SwitchParams) {
    const [status, setStatus] = useState(false);

    // Handle status changes
    const toggleStatus = () => {
        const newStatus = !status;
        setStatus(newStatus);
        onToggle(newStatus);
    }

    return (
        <div
            className={`switch-container ${status ? 'active' : ''}`}
            style={{ width: size }}
            onClick={toggleStatus}
        >
            <div className={`switch-slider ${status ? 'active' : ''}`}></div>
        </div>
    );
}