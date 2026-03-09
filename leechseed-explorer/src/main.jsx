import React from 'react'
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import LeechseedExplorer from './leechseed_system_explorer'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <LeechseedExplorer />
  </StrictMode>
)