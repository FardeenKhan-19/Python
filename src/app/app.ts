import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { SidebarComponent } from './layouts/sidebar/sidebar';
import { MainDashboardComponent } from './layouts/main-dashboard/main-dashboard';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    SidebarComponent,
    MainDashboardComponent
  ],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class AppComponent {
  title = 'TravelPlanner';
}