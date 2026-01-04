import { createContext, useContext, useState } from 'react';
import type { ReactNode } from 'react';

// Define the context type
interface SidebarContextType {
    isSidebarExpanded: boolean;
    toggleSidebar: () => void;
}

// Create the context
const SidebarContext = createContext<SidebarContextType | undefined>(undefined);

// Create a provider component
export const SidebarProvider = ({ children }: { children: ReactNode }) => {
    const [isSidebarExpanded, setIsSidebarExpanded] = useState(true);

    const toggleSidebar = () => {
        setIsSidebarExpanded((prev) => !prev);
    };

    return (
        <SidebarContext.Provider value={{ isSidebarExpanded, toggleSidebar }}>
            {children}
        </SidebarContext.Provider>
    );
};

// Custom hook to use the SidebarContext
export const useSidebar = () => {
    const context = useContext(SidebarContext);
    if (!context) {
        throw new Error('useSidebar must be used within a SidebarProvider');
    }
    return context;
};