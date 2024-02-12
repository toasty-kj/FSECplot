import { Component, OnInit } from '@angular/core'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  users: { userId: number; userName: string }[] = []
  currentTime = new Date()

  async ngOnInit() {
    this.users = await window.myAPI.loadUsers()
  }
}