import './globals.css'
import React from 'react'

export default function RootLayout({children}:{children:React.ReactNode}) {
  return (
    <html lang="en">
      <body className="bg-gray-100 text-gray-900">
        <main className="p-4">{children}</main>
      </body>
    </html>
  )
}
