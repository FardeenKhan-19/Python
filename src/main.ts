// In file: src/main.ts (REPLACE with this entire block)

import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app'; // FIX: Changed 'App' to 'AppComponent'

bootstrapApplication(AppComponent, appConfig) // FIX: Changed 'App' to 'AppComponent'
  .catch((err) => console.error(err));