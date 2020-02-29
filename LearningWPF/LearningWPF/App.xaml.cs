using System.Windows;
using LearningWPF.ViewModels;
using LearningWPF.Views;

namespace LearningWPF
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

            MainWindow startApp = new MainWindow();
            MotorViewModel viewModel = new MotorViewModel();
            startApp.DataContext = viewModel;
            startApp.Show();
        }
    }
}
