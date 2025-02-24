"use client"
import { MessageSquare, Sparkle, ChartNoAxesCombined, MapPinned } from "lucide-react"

import {
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar"

import { APP_TITLE } from "@/lib/constants"
import Link from "next/link"
import { ModeToggle } from "./mode-toggle"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"

// Menu items.
const items = [
    {
        title: "Dashboard",
        items: [
            {
                title: "User analytics",
                url: "/dashboard/user-analytics",
                icon: ChartNoAxesCombined,
            },
            {
                title: "User Heatmap",
                url: "/dashboard/user-heatmap",
                icon: MapPinned,
            }
        ]
    },

    {
        title: "Models",
        items: [
            {
                title: "Chat",
                url: "/chat",
                icon: MessageSquare,
            },
            {
                title: "Predict",
                url: "/predict",
                icon: Sparkle,
            },
        ],
    },
]


export function AppSidebar() {
    const pathname = usePathname();

    return (
        <Sidebar className="bg-zinc-900 dark:border-zinc-700 border-zinc-300">
            <SidebarHeader className="flex gap-0 flex-row justify-between py-3">
                <Link href="/" className="flex gap-2 items-center">
                    <img src="/fleurdelis.png" alt="Icon" className="h-6 w-6" />
                    <span className="text-sm">{APP_TITLE}</span>
                </Link>
                <ModeToggle />
            </SidebarHeader>
            <SidebarContent>
                {items.map((item) => (
                    <SidebarGroup key={item.title}>
                        <SidebarGroupLabel className="text-xxs"><b>{item.title}</b></SidebarGroupLabel>
                        <SidebarGroupContent>
                            <SidebarMenu>
                                {item.items.map((item) => {
                                    const isActive = pathname === item.url
                                    return <SidebarMenuItem key={item.title} >
                                        <SidebarMenuButton asChild className={cn("h-6", isActive && "dark:bg-zinc-800 bg-zinc-200")}>
                                            <a href={item.url} className="px">
                                                <item.icon className="text-purple-500" />
                                                <span className="text-xxs">{item.title}</span>
                                            </a>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                })}
                            </SidebarMenu>
                        </SidebarGroupContent>
                    </SidebarGroup>
                ))}
            </SidebarContent>
        </Sidebar>
    )
}
