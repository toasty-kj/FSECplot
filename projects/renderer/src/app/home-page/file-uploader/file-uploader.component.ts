import { Component, OnInit } from '@angular/core'

@Component({
  selector: 'app-file-uploader',
  templateUrl: './file-uploader.component.html',
  styleUrls: ['./file-uploader.component.css'],
})
export class FileUploaderComponent implements OnInit {
  users: { userId: number; userName: string }[] = []
  currentTime = new Date()

  async ngOnInit() {
    this.users = await window.myAPI.loadUsers()
  }
}
