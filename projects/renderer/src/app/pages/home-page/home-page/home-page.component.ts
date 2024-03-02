import { Component } from '@angular/core'
import { SendDataService } from '../../../service/send-data.service'
import { logoBase64 } from './logo-image'
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms'

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css'],
})
export class HomePageComponent {
  logoImage = logoBase64
  tag = ''
  title = ''
  filePath: string[] = []
  pathAndDefaultName: { path: string; name: string }[] = []
  dataNameList: FormGroup

  constructor(
    private api: SendDataService,
    private fb: FormBuilder,
  ) {
    this.dataNameList = this.fb.group({})
  }

  getTag(newTag: string) {
    this.tag = newTag
  }

  getInputTitle(newTitle: string) {
    this.title = newTitle
  }

  async getFilePath(newFilePath: string[]) {
    this.filePath = newFilePath
    // filepathからデフォルトのデータ名をバックエンドから取得する
    this.pathAndDefaultName = await this.api.getDefaultNameByFilePathList(
      this.filePath,
    )
    this.initFormArray()
  }

  async _onSubmit() {
    // TODO 入力のバリデーションを作成する
    const responce = await this.api.sendSelectedFilePathList(
      this.filePath,
      this.title,
      this.tag,
    )
    console.log(responce)
  }

  initFormArray() {
    // フォームグループを初期化する
    this.dataNameList = this.fb.group({})

    // 選択されたファイルの数だけフォームを作成する
    this.pathAndDefaultName.forEach((element, index) => {
      this.dataNameList.addControl(
        `control${index}`,
        new FormControl(element.name, Validators.required),
      )
    })
  }
}
