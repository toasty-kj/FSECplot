import { Component, ViewChild } from '@angular/core'
import { MessageService } from 'primeng/api'
import { SendDataService } from '../../../service/send-data.service'
import { logoBase64 } from './logo-image'
import { FormArray, FormBuilder, FormGroup, Validators } from '@angular/forms'
import {
  ToastContent,
  toastType,
} from '../../../components/shared/toast/toast-type'
@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  providers: [MessageService],
  styleUrls: ['./home-page.component.css'],
})
export class HomePageComponent {
  logoImage = logoBase64
  tag = ''
  title = ''
  filePath: string[] = []
  pathAndDefaultName: { path: string; name: string }[] = []
  dataNameList: FormGroup
  currentVersion = ''
  toastContent: ToastContent = { type: toastType.NotDefined, message: '' }
  isDownloading = false

  constructor(
    private api: SendDataService,
    private fb: FormBuilder,
  ) {
    this.dataNameList = this.fb.group({
      dataArray: this.fb.array([]),
    })
    this.getCurrentVersion()
    this.getDownloadingStatus()
    this.fetchUpdateHistory()
  }

  async getCurrentVersion() {
    this.currentVersion = await window.api.getVersion()
    this.toastContent = {
      type: toastType.Success,
      message: `you are using version ${this.currentVersion}`,
    }
  }

  async getDownloadingStatus() {
    // 5秒おきにダウンロードのステータスをmainに確認する
    setInterval(async () => {
      this.isDownloading = await window.api.getDownloadingStatus()
      console.log(this.isDownloading)
    }, 5000)
  }

  async fetchUpdateHistory() {
    const result = await window.api.readUpdateHistory()
    console.log(result)
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
    const isError = this.validateOnSubmit()
    if (isError) return

    const responce = await this.api.sendSelectedFilePathList(
      this.filePath,
      this.dataArray.value,
      this.title,
      this.tag,
    )
    console.log(responce)
  }

  validateOnSubmit() {
    let isError = false
    if (this.filePath.length == 0) {
      this.toastContent = {
        type: toastType.Error,
        message: 'Please input files',
      }
      isError = true
    }

    if (this.title == '') {
      this.toastContent = {
        type: toastType.Error,
        message: 'Please input title',
      }
      isError = true
    }

    if (this.tag == '') {
      this.toastContent = {
        type: toastType.Error,
        message: 'Please select fluorescence type for plotting',
      }
      isError = true
    }
    return isError
  }

  initFormArray() {
    // フォームグループを初期化する
    this.dataNameList = this.fb.group({
      dataArray: this.fb.array([], Validators.required),
    })

    // 選択されたファイルの数だけフォームを作成する
    this.pathAndDefaultName.forEach((element) => {
      ;(this.dataNameList.get('dataArray') as FormArray).push(
        this.fb.control(element.name),
      )
    })
  }

  get dataArray(): FormArray {
    return this.dataNameList.get('dataArray') as FormArray
  }
}
