import React from 'react'
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import BoldVentureExplorer from './bvx_system_explorer'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BoldVentureExplorer />
  </StrictMode>
)
