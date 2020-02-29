using LearningWPF.Models;
using System.Windows.Input;
using System.Windows;

namespace LearningWPF.ViewModels
{
    public class MotorViewModel : ProtoModel
    {
        #region Fields

        private int _motorId;
        private string _motorName;
        private Motor _currentMotor;
        private ICommand _getMotorCommand;
        private ICommand _saveMotorCommand;

        #endregion //Fields

        #region Properties

        public int MotorID
        {
            get { return _motorId; }
            set
            {
                if (value != _motorId)
                {
                    _motorId = value;
                    OnPropertyChanged("MotorID");
                }
            }
        }
        public string MotorName
        {
            get { return _motorName; }
            set
            {
                if (value != _motorName)
                {
                    _motorName = value;
                    OnPropertyChanged("MotorName");
                }
            }
        }
        public Motor CurrentMotor
        {
            get { return _currentMotor; }
            set
            {
                if (value != _currentMotor)
                {
                    _currentMotor = value;
                    OnPropertyChanged("CurrentMotor");
                }
            }
        }
        public ICommand SaveMotorCommand
        {
            get
            {
                if (_saveMotorCommand == null)
                {
                    _saveMotorCommand = new RelayCommand(
                        param => SaveMotor(),
                        param => (CurrentMotor != null)
                    );
                }
                return _saveMotorCommand;
            }
        }
        public ICommand GetMotorCommand
        {
            get
            {
                if (_getMotorCommand == null)
                {
                    _getMotorCommand = new RelayCommand(
                        param => GetMotor(),
                        param => MotorID > 0
                    );
                }
                return _getMotorCommand;
            }
        }

        #endregion //Properties

        #region Private Helpers

        private void GetMotor()
        {
            _currentMotor = new Motor(_motorId);
            _motorName = _currentMotor.MotorName;
            string msg = string.Format($"You got {_motorName}.");
            MessageBox.Show(msg);
        }

        private void SaveMotor()
        {
            string msg = string.Format($"You saved {_motorName}.");
            MessageBox.Show(msg);
        }

        #endregion Private Helpers
    }
}
