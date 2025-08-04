// src/main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { AppComponent } from './app/app.component';
import { appConfig } from './app/app.config'; // Import your app's configuration

// This is the correct way to start a modern standalone Angular application
bootstrapApplication(AppComponent, appConfig)
  .catch(err => console.error(err));
