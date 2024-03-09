const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('api', {
  getVersion: (): Promise<string> => {
    return ipcRenderer.invoke('getVersion')
  },
  getDownloadingStatus: (): Promise<boolean> => {
    return ipcRenderer.invoke('getDownloadingStatus')
  },
  readUpdateHistory: (): Promise<JSON> => {
    return ipcRenderer.invoke('readUpdateHistory')
  },
})
