"use client"
import { MessageSquare, Sparkle } from "lucide-react"

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
import Image from "next/image"
import { ModeToggle } from "./mode-toggle"

// Menu items.
const items = [
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
                        <SidebarGroupLabel>{item.title}</SidebarGroupLabel>
                        <SidebarGroupContent>
                            <SidebarMenu>
                                {item.items.map((item) => (
                                    <SidebarMenuItem key={item.title} className="text-xxs">
                                        <SidebarMenuButton asChild>
                                            <a href={item.url} >
                                                <item.icon className="text-purple-500" />
                                                <span className="text-xs">{item.title}</span>
                                            </a>
                                        </SidebarMenuButton>
                                    </SidebarMenuItem>
                                ))}
                            </SidebarMenu>
                        </SidebarGroupContent>
                    </SidebarGroup>
                ))}
            </SidebarContent>
        </Sidebar>
    )
}
