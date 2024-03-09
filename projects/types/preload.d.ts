export interface API {
  getVersion: () => Promise<string>
  getDownloadingStatus: () => Promise<boolean>
}

declare global {
  interface Window {
    api: API
  }
}
