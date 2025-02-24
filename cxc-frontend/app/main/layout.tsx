import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
import { ReactNode } from "react";

interface MainLayoutProps {
    children: ReactNode;
}

export default function MainLayout({ children }: MainLayoutProps) {
    return (
        <SidebarProvider>
            <div className="h-lvh w-screen flex">
                <AppSidebar />
                <main className="h-full w-full relative overflow-auto">
                    {/* <SidebarTrigger className="absolute z-10" /> */}
                    {children}
                </main>
            </div>
        </SidebarProvider>
    )
}